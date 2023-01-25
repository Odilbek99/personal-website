from django.shortcuts import render
from .models import NavBarModel, HomePageModel
# Create your views here.
def index(request):
    navbar = NavBarModel.objects.all()
    home = HomePageModel.objects.all()
    context = {
        'navbar': navbar,
        'home': home
    }
    return render(request, 'index.html', context=context)

def portfolio_details(request):
    return render(request, 'portfolio-details.html')
