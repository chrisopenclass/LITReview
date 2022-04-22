from django.urls import path
from .views import SubscriptionSupp

from. import views


urlpatterns = [
    path('', views.abonnement, name='abonnement'),
    path('SubscriptionSupp/<int:pk>',
         SubscriptionSupp.as_view(),
         name='SubscriptionSupp')
]
