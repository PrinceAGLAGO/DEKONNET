from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Utilisateur

class InscriptionForm(UserCreationForm):
    class Meta:
        model = Utilisateur

        fields = [
            'email', 'nom', 'prenom', 'telephone',
            'date_naissance', 'adresse_geo', 'mode_paiment',
            'password1', 'password2'
        ]
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'adresse_geo': forms.TextInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'mode_paiment': forms.Select(attrs={'class': 'form-control'}),
        }

class ConnexionForm(AuthenticationForm):
    username = forms.EmailField(
        label="Adresse email",
        widget=forms.EmailInput(attrs={'autofocus': True})
    )