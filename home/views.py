from django.shortcuts import render
from . import models 

# Create your views here.

def index(request):
    data = {
        'equipe1': models.EquipeA.objects.filter(status=True),
        'equipe2': models.EquipeB.objects.filter(status=True)
    }
  
    return render(request, 'pages/index.html')

def schedule(request):
    return render(request, 'pages/schedule.html')


def liverpool(request):
    return render(request, 'pages/liverpool.html')

def league_table(request):
    return render(request, 'pages/league-table.html')

def soccer_about_us_1(request):
    return render(request, 'pages/soccer-about-us-1.html')

def single_post(request):
    return render(request, 'pages/standard-post-type.html')

def acoordions_toggle(request):
    return render(request, 'pages/accordions-toggles.html')



    