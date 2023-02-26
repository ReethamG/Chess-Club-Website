from django.contrib import admin

# Register your models here.
from website.models import Annoucement, Meeting

class AnnoucementAdmin(admin.ModelAdmin):
    pass

class MeetingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Annoucement, AnnoucementAdmin)
admin.site.register(Meeting, MeetingAdmin)
