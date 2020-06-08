from django.db import models

# Create your models here.

class Joueur(models.Model):
    nom = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='player/photo', blank='True', null='True')

    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "joueur"
        verbose_name_plural = "Nom joueurs"

    def __str__(self):
        return self.nom

    

class Infojoueur(models.Model):
    nationality = models.CharField(max_length=200)
    drapeau = models.ImageField(upload_to='home/drapeau')
    position= models.CharField(max_length=200)
    club = models.CharField(max_length=200)
    Joueur = models.ForeignKey(Joueur, on_delete=models.CASCADE, related_name="foot")

    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Information joueur'
        verbose_name_plural = 'Information des joueurs'

    def __str__(self):
        return self.nationality
    
    @property
    def getNom(self):
        return self.Joueur