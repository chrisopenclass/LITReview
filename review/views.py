from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from itertools import chain
from django.db.models import CharField, Value

from .forms import FormulaireTicket, FormulaireRevue
from .models import Ticket, Review


@login_required
def creer_ticket(request):
    titre = "Créer un ticket"
    if request.method == "POST":
        try:
            Ticket.objects.create(titre=request.POST['titre'],
                                  description=request.POST['description'],
                                  user=request.user
                                  )
        except Exception:
            form = FormulaireTicket(request.POST, request.FILES)
        else:
            messages.success(request, 'Ticket créé !')
            return redirect("tableau_de_bord")
    else:
        form = FormulaireTicket(request.POST, request.FILES)
    return render(request, 'review/creer_ticket.html', {'titre': titre,
                                                        'form_ticket': form
                                                        })


@login_required
def creer_revue(request):
    titre = "Créer une review"
    if request.method == "POST":
        try:
            ticket_instance = Ticket.objects.create(
                                    titre=request.POST['titre'],
                                    description=request.POST['content'],
                                    user=request.user
                                    )
            Review.objects.create(ticket=ticket_instance,
                                  titre=request.POST['titre'],
                                  note=request.POST['note'],
                                  content=request.POST['content'],
                                  user=request.user
                                  )
        except Exception:
            form_review = FormulaireRevue(request.POST)
            form_ticket = FormulaireTicket(request.POST)
        else:
            messages.success(request, 'Review créée !')
            return redirect("tableau_de_bord")
    else:
        form_review = FormulaireRevue()
        form_ticket = FormulaireTicket()
    return render(request, 'review/creer_revue.html', {
                                                    'titre': titre,
                                                    'form_review': form_review,
                                                    'form_ticket': form_ticket
                                                    })


@login_required
def creer_revue_ticket(request, id_ticket=None):
    titre = "Créer une review"

    existing_ticket = Ticket.objects.get(pk=id_ticket)

    if request.method == "POST":
        try:
            Review.objects.create(ticket=existing_ticket,
                                  titre=request.POST['titre'],
                                  note=request.POST['note'],
                                  content=request.POST['content'],
                                  user=request.user
                                  )
            print(Review.content)
        except Exception:
            form_review = FormulaireRevue(request.POST)
        else:
            messages.success(request, 'Review créée !')
            return redirect("tableau_de_bord")
    else:
        form_review = FormulaireRevue()
    return render(request, 'review/creer_revue_ticket.html', {
                                            'titre': titre,
                                            'form_review': form_review,
                                            'existing_ticket': existing_ticket
                                            })


@login_required
def tableau_de_bord(request):
    current_user = request.user

    followers = current_user.following.all()
    followers_id = []
    for follower in followers:
        followers_id.append(follower.followed_user.pk)

    ids_of_ticket_answerers = []
    for ticket in Ticket.objects.filter(user=current_user):
        for review in Review.objects.all():
            if review.ticket == ticket:
                ids_of_ticket_answerers.append(review.user.pk)

    reviews = (Review.objects.filter(user=request.user) |
               Review.objects.filter(user_id__in=followers_id) |
               Review.objects.filter(user_id__in=ids_of_ticket_answerers)
               )

    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    followers = current_user.following.all()
    followers_list = []
    for follower in followers:
        followers_list.append(follower.followed_user.pk)

    tickets = (Ticket.objects.filter(user_id__in=followers_list) |
               Ticket.objects.filter(user=request.user)
               )
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.date_creation,
        reverse=True
        )
    return render(request, 'review/tableau_de_bord.html', context={'posts': posts})


@login_required
def posts(request):
    titre = "Posts"
    current_user = request.user
    tickets = Ticket.objects.filter(user=current_user)
    reviews = Review.objects.filter(user=current_user)
    context = {"titre": titre,
               "tickets": tickets,
               "reviews": reviews,
               "current_user": current_user,
               }
    return render(request, "review/posts.html", context)


class TicketMaj(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket
    form_class = FormulaireTicket
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('posts')

    def test_func(self):
        ticket = self.get_object()
        if self.request.user == ticket.user:
            return True
        return False


class TicketDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ticket
    success_url = reverse_lazy('posts')

    def test_func(self):
        ticket = self.get_object()
        if self.request.user == ticket.user:
            return True
        return False


class ReviewUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = FormulaireRevue
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('posts')

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False


class ReviewDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('posts')

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False
