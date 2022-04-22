from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import UserFollows


class NouveauxAbonnement(ModelForm):

    class Meta:
        model = UserFollows
        fields = ['followed_user']
        labels = {"followed_user": ""}
        widgets = {'followed_user': forms.TextInput()}

    def _clean_fields(self):
        breakpoint()
        return super()._clean_fields()

    def is_valid(self):
        breakpoint()
        return super().is_valid()

    def clean_followed_user(self):
        breakpoint()
        followed_user = self.cleaned_data['followed_user']
        user = User.objects.get(id=self.request.user.id)
        print(followed_user)
        print(user)
        print(followed_user == user)
        if followed_user == user:
            raise ValueError('Vous ne pouvez pas vous ajouter')
        else:
            return followed_user
