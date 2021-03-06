from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .forms import NouveauxAbonnement
from .models import UserFollows


@login_required
def abonnement(request):
    titre = "Onglet d'abonnements"
    user_follows = UserFollows.objects.all()
    user = request.user
    name = request.user.username
    subscribers = user.followed_by.all()
    if request.method == "POST":
        entry = request.POST['followed_user']
        if not entry != name:
            formulaire = NouveauxAbonnement(request.POST)
            messages.error(request, 'Vous ne pouvez pas vous ajouter')
        else:
            try:
                user_to_follow = User.objects.get(username=entry)
                UserFollows.objects.create(user=request.user,
                                           followed_user=user_to_follow,
                                           )
            except Exception:
                formulaire = NouveauxAbonnement(request.POST)
                messages.error(request, 'Erreur')
            else:
                messages.success(request, "Utilisateur suivi !")
                return redirect("abonnement")
    else:
        formulaire = NouveauxAbonnement()
    return render(request, 'sub_system/abonnement.html', {
                                                'titre': titre,
                                                'form': formulaire,
                                                'current_user': user,
                                                'subscribers': subscribers,
                                                'user_follows': user_follows
                                                })


class SubscriptionSupp(LoginRequiredMixin,
                       DeleteView,
                       SuccessMessageMixin
                       ):
    model = UserFollows
    success_url = reverse_lazy('abonnement')
    success_message = "Abonnement r??sili??"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = User.objects.get(id=self.request.user.id)
        context['followed_user'] = UserFollows.objects.exclude(
                                                            user=current_user)
        return context
