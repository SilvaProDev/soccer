from django.contrib import admin
from .models import  InfoCoach, OriginCoach, Categorie, InfoJoueur, Player
# Register your models here.

class InfoCoachAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'date_add',
        'date_upd',
        
    )
    list_filter = (
        'nom',
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
                
                'image',
            ]
        }),
        
    ]
class OriginCoachchAdmin(admin.ModelAdmin):
    list_display = (
        'nationality',
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
                'cate',
                'nationality',
                'team',
                'photo',
                
                
            ]
        }),
        
    ]

class CategorieAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'date_add',
        'date_upd',
        
    )
    list_filter = (
        'status',
    )
    search_fields = (
        'status',
    )
    list_per_page = 10
    date_hierarchy = 'date_add'
    fieldsets = [
        ('Info',{
            'fields': [
                'titre',
                
            ]
        }),
        ('Satatus et Activation',{
            'fields': [
                'status',         
            ]
        }),
        
    ]

class InfoJoueurAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'taille',
        'poids',
        
    )
    list_filter = (
        'nom',
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
                'taille',
                'poids',
                
            ]
        }),
        
    ]

class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'nom',
        'categories',
        'date_add',
        'date_upd',
        
    )
    list_filter = (
        'nom',
    )
    search_fields = (
        'nom',
    )
    list_per_page = 10
    date_hierarchy = 'date_add'
    fieldsets = [
        ('Info',{
            'fields': [
                'categories',
                'number',
                'nom',
                'infojoueurs',       
            ]
        }),
        
    ]


admin.site.register(InfoCoach, InfoCoachAdmin)
admin.site.register(OriginCoach, OriginCoachchAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(InfoJoueur, InfoJoueurAdmin)
admin.site.register(Player, PlayerAdmin)


