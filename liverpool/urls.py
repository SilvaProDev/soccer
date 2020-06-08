from django.urls import path

from . import views
app_name ='liverpool'
urlpatterns = [
    
    path('', views.liverpool, name='liverpool'),
    
]