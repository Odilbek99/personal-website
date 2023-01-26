from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.StatsModel)
admin.site.register(models.AboutModel)
admin.site.register(models.HomePageModel)
admin.site.register(models.NavBarModel)
admin.site.register(models.InterestModel)

@admin.register(models.SkillsModel)
class SkillsModelAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Sales Summary', {
            'fields': (
                ('skill','percentage','progress'),
            )
        }),
    )
    readonly_fields = [
        'progress'
    ]
    list_display = ['skill','progress']

