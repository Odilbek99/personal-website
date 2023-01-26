from django.shortcuts import render
from .models import NavBarModel, HomePageModel, AboutModel, StatsModel, SkillsModel
# Create your views here.
def index(request):
    navbar = NavBarModel.objects.all()
    home = HomePageModel.objects.all()
    about = AboutModel.objects.get(id=1)
    stats = StatsModel.objects.all()
    skills = SkillsModel.objects.all()

    context = {
        'navbar': navbar,
        'home': home,
        'about': about,
        'stats': stats,
        'skills': skills,
        'first_skills': skills[:len(skills)//2],
        'last_skills': skills[len(skills)//2:]
     }
    return render(request, 'index.html', context=context)

def portfolio_details(request):
    return render(request, 'portfolio-details.html')
