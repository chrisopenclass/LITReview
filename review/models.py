from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# model servant pour la migration migration affin de créer les éléments dans la BDD

class Ticket(models.Model):
    # model des tickets pour la bdd
    titre = models.CharField(max_length=128, blank=False)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse("ticket", kwargs={"pk": self.pk})


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    note = models.PositiveSmallIntegerField(
        # validation de la note
        validators=[MinValueValidator(0),
                    MaxValueValidator(5)],
        verbose_name='note')
    titre = models.CharField(max_length=128, verbose_name='Titre de la critique')
    content = models.TextField(max_length=8192, blank=True, verbose_name='Commentaire')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse("review", kwargs={"pk": self.pk})
