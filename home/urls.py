from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('schedule', views.schedule, name='schedule'), 
    path('soccer', views.soccer_about_us_1, name='soccer'),
    path('league', views.league_table, name='league'),
    path('single', views.single_post, name='single'),
    path('toggle', views.acoordions_toggle, name='toggle'),
]