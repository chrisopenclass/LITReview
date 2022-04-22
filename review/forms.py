from django import forms
from .models import Ticket, Review


class FormulaireTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description']

        labels = {"title": "Titre",
                  "description": "Description"
                  }


class FormulaireRevue(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['titre', 'note', 'content']
        labels = {"titre": "Titre de la critique",
                  "note": "note",
                  "content": "Commentaire"
                  }
        choix = [(0, '0'),
                 (1, '1'),
                 (2, '2'),
                 (4, '3'),
                 (4, '4'),
                 (5, '5')
                 ]
        widgets = {"note": forms.RadioSelect(choices=choix),
                   "content": forms.Textarea()
                   }
