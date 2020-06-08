from django.contrib import admin
from .models import EquipeA, EquipeB
# Register your models here.

class EquipeAAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'isProgrammed',
        'date_add',
        'date_upd',
        'status',
    )
    list_filter = (
        'isProgrammed',
    )
    search_fields = (
        'nom',
    )
    list_per_page = 6
    date_hierarchy = 'date_add'
    fieldsets = [
        ('Info', {
            'fields': [
                'nom',
                'image',
                'score',
                
            ]
        }),
        ('Programmation', {
            'fields':[
                'isProgrammed',
            ]
        }),
        ('Programmation', {
            'fields':[
                'status',
            ]
        })
    ]

class EquipeBAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'isProgrammed',
        'photo',
        'rencontre',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'isProgrammed',
    )
    search_fields = (
        'nom',
    )
    list_per_page = 6
    date_hierarchy = 'date_add'
    fieldsets = [
        ('Info', {
            'fields': [
                'nom',
                'rencontre',
                'photo',
                'score',
                'lieu',
            ]
        }),
        ('Programmation', {
            'fields':[
                'isProgrammed',
            ]
        }),
        ('Programmation', {
            'fields':[
                'status',
            ]
        })
    ]



admin.site.register(EquipeA, EquipeAAdmin)
admin.site.register(EquipeB, EquipeBAdmin)
