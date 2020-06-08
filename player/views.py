from django.shortcuts import render
from . import models 

# Create your views here.
def player(request):
    dat = {
        'players': models.Joueur.objects.filter(status=True),
        'infos': models.Infojoueur.objects.all()
    }
    return render(request, 'player/player-details.html', dat)
