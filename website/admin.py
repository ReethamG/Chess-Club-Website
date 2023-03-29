from django.contrib import admin

# Register your models here.
from website.models import Announcement, Meeting

class AnnouncementAdmin(admin.ModelAdmin):
    pass

class MeetingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Meeting, MeetingAdmin)
