from django.contrib import admin
from .models import HomePageModel,NavBarModel,StatsModel, AboutModel

# Register your models here.

admin.site.register(StatsModel)
admin.site.register(AboutModel)
admin.site.register(HomePageModel)
admin.site.register(NavBarModel)


