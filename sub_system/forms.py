from django import forms
from django.forms import ModelForm

from .models import UserFollows


class NouveauxAbonnement(ModelForm):

    class Meta:
        model = UserFollows
        fields = ['followed_user']
        labels = {"followed_user": ""}
        widgets = {'followed_user': forms.TextInput()}
