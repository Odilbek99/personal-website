from django.shortcuts import render
from .models import NavBarModel, HomePageModel, AboutModel, StatsModel
# Create your views here.
def index(request):
    navbar = NavBarModel.objects.all()
    home = HomePageModel.objects.all()
    about = AboutModel.objects.get(id=1)
    stats = StatsModel.objects.all()
    context = {
        'navbar': navbar,
        'home': home,
        'about': about,
        'stats': stats,
    }
    return render(request, 'index.html', context=context)

def portfolio_details(request):
    return render(request, 'portfolio-details.html')
