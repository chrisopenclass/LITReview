from django.urls import path
from . import views


urlpatterns = [
    path('', views.tableau_de_bord, name='tableau_de_bord'),
    path('posts', views.posts, name='posts'),
    path('creer_ticket', views.creer_ticket, name='creer_ticket'),
    path('creer_revue', views.creer_revue, name='creer_revue'),

    path('creer_revue_ticket/<int:id_ticket>/',
         views.creer_revue_ticket,
         name='creer_revue_ticket'
         ),
    path('ticket/<int:pk>/update',
         views.TicketMaj.as_view(),
         name='ticket-update'
         ),
    path('ticket/<int:pk>/delete',
         views.TicketDelete.as_view(),
         name='ticket-delete'
         ),
    path('review/<int:pk>/update',
         views.ReviewUpdate.as_view(),
         name='review-update'
         ),
    path('review/<int:pk>/delete',
         views.ReviewDelete.as_view(),
         name='review-delete'
         )
]
