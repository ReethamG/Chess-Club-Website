from django.shortcuts import render
from website.models import Annoucement, Meeting


# Create your views here.
def home(request):
    annoucements = Annoucement.objects.all()
    meetings = Meeting.objects.all()
    context = {
        "annoucements": annoucements,
        "meetings": meetings,
    }
    return render(request, 'home.html', context)

def join(request):
    return render(request, 'join.html', {})

def about_us(request):
    return render(request, 'about_us.html', {})