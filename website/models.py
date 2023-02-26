from django.db import models

class Annoucement(models.Model):
    message = models.CharField(max_length=255)
    def __str__(self):
        return self.message

class Meeting(models.Model):
    message = models.CharField(max_length=255)
    def __str__(self):
        return self.message