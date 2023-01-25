from django.db import models

# Create your models here.
class HomePageModel(models.Model):
    full_name = models.CharField(max_length=50)
    fisrt_part = models.TextField(default=None)
    whoami = models.TextField(default=None)
    second_part = models.TextField(default=None)

    def __str__(self) -> str:
        return self.full_name

class NavBarModel(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title