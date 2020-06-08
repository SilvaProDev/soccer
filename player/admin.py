from django.contrib import admin
from .models import  Joueur, Infojoueur
# Register your models here.

class JoueurAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'date_add',
        'date_upd',
        'status',
    )
    list_filter = (
        'status',
    )
    search_fields = (
        'nom',
    )
    list_per_page = 10
    date_hierarchy = 'date_add'
    fieldsets = [
        ('Info',{
            'fields': [
                'nom',
                'photo',
            ]
        }),
        ('Status et Activation',{
            'fields': [
                'status',
            ]
        })
    ]

class InfojoueurAdmin(admin.ModelAdmin):
    list_display = (
        'nationality',
        'position',
        'club',
        'date_add',
        'date_upd',
        
    )
    list_filter = (
        'nationality',
    )
    search_fields = (
        'nationality',
    )
    list_per_page = 10
    date_hierarchy = 'date_add'
    fieldsets = [
        ('Info',{
            'fields': [
                'Joueur',
                'nationality',
                'position',
                'club',
                'drapeau',
                
            ]
        }),
        
    ]

admin.site.register(Joueur, JoueurAdmin)
admin.site.register(Infojoueur, InfojoueurAdmin)
