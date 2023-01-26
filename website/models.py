from django.db import models
from django.utils.html import format_html
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
    image = models.ImageField(upload_to='assets/img/', default=None)


    def __str__(self) -> str:
        return self.whoami


class StatsModel(models.Model):
    title = models.CharField(max_length=255, help_text='Projects, Awards etc..')
    number = models.IntegerField(help_text='Projects, Awards etc..')
    icon = models.CharField(max_length=255, help_text='ccopy icon class from https://icons.getbootstrap.com/')

    def __str__(self) -> str:
        return self.title
    
class SkillsModel(models.Model):
    skill = models.CharField(max_length=255, help_text='ex: Python, JS, JAVA, C++')
    percent = models.IntegerField(help_text='Projects, Awards etc..')
   
    def percentage_paid(self):
        if self.paid_amount and self.final_price:
            percentage = round((self.paid_amount / self.final_price * 100), 2)
        else:
            percentage = 0
        return format_html(
            '''
            <progress value="{0}" max="100"></progress>
            <span style="font-weight:bold">{0}%</span>
            ''',
            percentage
        )

    def __str__(self) -> str:
        return self.skill