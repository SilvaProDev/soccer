from django.db import models

# Create your models here.

class InfoCoach(models.Model):
    nom = models.CharField(max_length=200)
    image = models.ImageField(upload_to='liverpool/image', null='True', blank='True')

    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Infocoach'
        verbose_name_plural = 'Info sur le Coach'

    def __str__(self):
        return self.nom

class OriginCoach(models.Model):
    nationality = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='liverpool/photo', blank='True', null='True')
    cate = models.ForeignKey(InfoCoach, on_delete=models.CASCADE, related_name='info')
    team = models.CharField(max_length=255)

    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "origin"
        verbose_name_plural = "Origine Coach"

    def __str__(self):
        return self.nationality

class Categorie(models.Model):
    titre = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Les categories"
    
    def __str__(self):
        return self.titre

class InfoJoueur(models.Model):
    nom = models.CharField(max_length=200)
    taille = models.CharField(max_length=25)
    poids = models.CharField(max_length=25)

    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "info joueur"
        verbose_name_plural = "Infos joueur"

    def __str__(self):
        return self.nom


class Player(models.Model):
    number = models.IntegerField()
    nom = models.CharField(max_length=255)
    categories = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='menu')
    infojoueurs = models.OneToOneField(InfoJoueur, on_delete=models.CASCADE)

    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "player"
        verbose_name_plural = "Players"

    def __str__(self):
        return self.nom



    