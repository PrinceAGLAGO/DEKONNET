from django import forms
from django.forms import ModelForm
from .models import Annonce, Exigence


class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = ['titre','categorie_article', 'user_contact', 'article_image', 'description', 'type_annonce', 'etiquette']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'user_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'article_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'type_annonce': forms.Select(attrs={'class': 'form-control'}),
            'etiquette': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ExigenceForm(forms.ModelForm):
    class Meta:
        model = Exigence
        fields = ['description_exigence', 'option_additionnelle']
        widgets = {
            'description_exigence': forms.Textarea(attrs={'class': 'form-control'}),
            'option_additionnelle': forms.TextInput(attrs={'class': 'form-control'}),
        }