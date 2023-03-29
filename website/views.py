from django.shortcuts import render
from website.models import Announcement, Meeting


# Create your views here.
def home(request):
    announcements = Announcement.objects.all()
    meetings = Meeting.objects.all()
    context = {
        "announcements": announcements,
        "meetings": meetings,
    }
    return render(request, 'home.html', context)

def about_us(request):
    return render(request, 'about_us.html', {})