from django import forms
from django.forms import ModelForm
from .models import Annonce, Exigence


class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = [
            'titre',
            'categorie_article',
            'type_annonce',
            'description',
            'prix',
            'article_image',
            'user_contact',
            'etiquette'
        ]

        widgets = {
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Titre de votre annonce'
            }),
            'categorie_article': forms.Select(attrs={
                'class': 'form-control'
            }),
            'type_annonce': forms.Select(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description détaillée',
                'rows': 4
            }),
            'prix': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Prix (si applicable)'
            }),
            'article_image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'user_contact': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre numéro de téléphone'
            }),
            'etiquette': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Mots-clés (séparés par des virgules)'
            })
        }

        labels = {
            'titre': 'Titre',
            'categorie_article': 'Catégorie',
            'type_annonce': 'Type d\'annonce',
            'description': 'Description',
            'prix': 'Prix',
            'article_image': 'Image de l\'article',
            'user_contact': 'Contact',
            'etiquette': 'Mots-clés'
        }

        help_texts = {
            'titre': 'Donnez un titre clair et descriptif à votre annonce',
            'description': 'Décrivez votre article en détail',
            'prix': 'Laissez vide si vous souhaitez échanger',
            'article_image': 'Ajoutez une photo claire de votre article',
            'user_contact': 'Numéro de téléphone pour être contacté',
            'etiquette': 'Ex: smartphone, occasion, neuf, etc.'
        }


class ExigenceForm(forms.ModelForm):
    class Meta:
        model = Exigence
        fields = ['description_exigence', 'option_additionnelle']
        widgets = {
            'description_exigence': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Décrivez vos exigences',
                'rows': 3
            }),
            'option_additionnelle': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Options supplémentaires'
            }),
        }
        labels = {
            'description_exigence': 'Exigences',
            'option_additionnelle': 'Options'
        }
        help_texts = {
            'description_exigence': 'Décrivez ce que vous attendez en échange',
            'option_additionnelle': 'Autres conditions ou informations'
        }