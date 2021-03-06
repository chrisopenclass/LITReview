from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    titre = "S'enregistrer"
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compte créé avec succès !')
            return redirect('connexion')

    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form,
                                                            'titre': titre
                                                            })
