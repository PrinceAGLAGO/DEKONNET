from django.db import models
from utilisateurs.models import Utilisateur
# Create your models here.




class Annonce(models.Model):
    TROC='T'
    VENTE='V'
    ACHAT='A'
    TYPE_CHOICES=[
        (TROC,'troc'),
        (VENTE,'vente'),
        (ACHAT,'achat'),
    ]


    titre=models.CharField(max_length=25)
    user=models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    type_annonce=models.CharField(max_length=1, choices=TYPE_CHOICES, default=TROC)
    user_contact=models.CharField(max_length=25)
    article_image = models.CharField(max_length=25, blank=True)
    description=models.TextField()
    categorie_article = models.CharField(max_length=30)
    prix=models.DecimalField(max_digits=10, decimal_places=2)
    date_publication=models.DateTimeField(auto_now_add=True)
    statut=models.CharField(max_length=10, default='actif')
    etiquette=models.CharField(max_length=9)
    promotion_disponible=models.BooleanField(default=False)

    def __str__(self):
        return self.titre
    
class Exigence(models.Model):
    annonce=models.ForeignKey(Annonce, on_delete=models.CASCADE)
    description_exigence=models.TextField()
    option_additionnelle=models.CharField(max_length=25, blank=True)

