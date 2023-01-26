from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    navbar = models.NavBarModel.objects.all()
    home = models.HomePageModel.objects.all()
    about = models.AboutModel.objects.get(id=1)
    stats = models.StatsModel.objects.all()
    skills = models.SkillsModel.objects.all()
    interests = models.InterestModel.objects.all()
    testimonials = models.TestimonialModel.objects.all()

    context = {
        'navbar': navbar,
        'home': home,
        'about': about,
        'stats': stats,
        'skills': skills,
        'interests': interests,
        'testimonials': testimonials,
        'first_skills': skills[:len(skills)//2],
        'last_skills': skills[len(skills)//2:]
     }
    return render(request, 'index.html', context=context)

def portfolio_details(request):
    return render(request, 'portfolio-details.html')
