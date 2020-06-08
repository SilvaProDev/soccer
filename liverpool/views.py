from django.shortcuts import render
from . import models 

# Create your views here.
def liverpool(request):
    data = {
        'coachs':models.InfoCoach.objects.all(),
        'infos':models.OriginCoach.objects.all(),
        'categories': models.Categorie.objects.all(),
        'infojoueurs': models.InfoJoueur.objects.all(),
        'players': models.Player.objects.all()
    }
    return render(request, 'pages/liverpool.html',data)