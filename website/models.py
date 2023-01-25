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

class AboutModel(models.Model):
    DEGREE_CHOICES = (
    ("BACHELOR", "Bachelor"),
    ("MASTER", "Master"),
    ("PHD", "PhD"),
    )

    FREELANCE_CHOICES = (
    ("AVAILABLE", "Available"),
    ("NOT_AVAILABLE", "Not Available")
    )

    title = models.CharField(max_length=255, default='LEARN MORE ABOUT ME')
    whoami = models.CharField(max_length=255, default='Data Scientist/Python Developer')
    birthday = models.DateField()
    website = models.URLField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=25)
    age = models.IntegerField()
    degree = models.CharField(max_length=25, choices=DEGREE_CHOICES, default='BACHELOR')
    email = models.EmailField(max_length=255)
    freelance =  models.CharField(max_length=25, choices=FREELANCE_CHOICES, default='NOT AVAILABLE')
    about_me = models.TextField()

class StatsModel(models.Model):
    title = models.CharField(max_length=255, help_text='Projects, Awards etc..')
    number = models.IntegerField(help_text='Projects, Awards etc..')
    icon = models.CharField(max_length=255, help_text='ccopy icon class from https://icons.getbootstrap.com/')
    about = models.ForeignKey(AboutModel, on_delete=models.CASCADE, related_name='stats')