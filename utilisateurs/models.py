from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator, EmailValidator, FileExtensionValidator



# Create your models here.
class UtilisateurManager( BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'adresse e-mail est obligatoire')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superutilisateur', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Le superutilisateur doit avoir is_staff=True.')
        
        if extra_fields.get('is_superutilisateur') is not True:
            raise ValueError('Le superutilisateur doit avoir is_superutilisateur=True.')

        return self.create_user(email, password, **extra_fields)


class Utilisateur(AbstractUser):

    MODE_PAIEMENT_CHOICES = [
        ('carte', 'Carte Bancaire'),
        ('mobileMo', 'Mobile Money'),
        ('paypal', 'PayPal'),
        ('especes', 'Espèces'),
    ]

    username = None
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    nom = models.CharField(max_length=30, validators=[MinLengthValidator(2), MaxLengthValidator(30)])
    prenom = models.CharField(max_length=30, validators=[MinLengthValidator(2), MaxLengthValidator(30)])
    telephone = models.CharField(max_length=15, unique=True, validators=[RegexValidator(regex=r'^(\+228)?\d{8,15}$', message="Entrez un numéro togolais valide à 8 chiffres, avec ou sans +228")])
    date_naissance = models.DateField(null=True, blank=True)
    photo_profil = models.CharField(max_length=25, blank=True, default='default.jpg')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superutilisateur = models.BooleanField(default=False)
    adresse_geo=models.CharField(max_length=50, blank=True)
    mode_paiment=models.CharField(max_length=50, blank=True, choices=MODE_PAIEMENT_CHOICES,default='carte')
    date_inscription=models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom', 'telephone']

    objects = UtilisateurManager()

    def __str__(self):
        return self.email

    def utilisateurConnecter(self):
        return f"{self.prenom}{self.nom}"
    #les methodes 

    def seConnecter(self, password):
        self.set_password(password)
        self.save()
    def seDeconnecter(self):
        self.is_active = False
        self.save()
    def changerMotDePasse(self, password):
        self.set_password(password)
        self.save() 
    
    # def changerPhotoProfile(self):
    #     self.photo_profil =
    #     self.save()
    