from django.urls import path
from django.contrib.auth import views as auth_views

from. import views


urlpatterns = [
    path('register/', views.register, name='registration'),
    path('',
         auth_views.LoginView.as_view(template_name='authentication/connexion.html'),
         name='connexion'),
    path('deconnexion/',
         auth_views.LogoutView.as_view(template_name='authentication/deconnexion.html'),
         name='deconnexion'),
]
