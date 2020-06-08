from django.db import models

# Create your models here.

class EquipeA(models.Model):
    nom = models.CharField(max_length=250)
    image = models.ImageField(upload_to='home/image', null='True', blank='True')
    isProgrammed = models.BooleanField(default=True)
    score = models.IntegerField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "L'équipe A"
        verbose_name_plural = "Equipes_poule_A"

    def __str__(self):
        return self.nom 

class EquipeB(models.Model):
    nom = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='home/equipeB/photo', null='True', blank='True')
    isProgrammed = models.BooleanField(default=True)
    #equipe = models.ForeignKey(EquipeA, on_delete=models.CASCADE)
    rencontre = models.DateTimeField()
    lieu = models.CharField(max_length=200)
    score = models.IntegerField()
    status = models.BooleanField(default=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True) 

    class Meta:
        verbose_name = "L'équipe A"
        verbose_name_plural = "Equipes_poule_B"

    def __str__(self):
        return self.nom


    
