from django.shortcuts import render
from .models import Iccfixture

# Create your views here.
def home(requset):
    return render(requset, 'index.html')

def search_fixture(requset):
    if requset.method == 'POST':
        team = requset.POST['team']
        fixture = Iccfixture.objects.filter(team1__contains=team)
        return render(requset, 'index.html', {'fixture': fixture})
       
    



