from django.db import models



class Sms(models.Model):
    smsc = models.CharField(max_length=50)
    timestamp = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    release_date = models.DateField()
