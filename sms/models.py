from django.db import models

# Create your models here.
#參考參數https://docs.djangoproject.com/zh-hans/3.2/ref/models/fields/#django.db.models.CharField.max_length
class Sms(models.Model):
    smsc = models.CharField(max_length=15)
    timestamp = models.CharField(max_length=25)
    text = models.CharField(max_length=75)
    number = models.CharField(max_length=15)

    class Meta:
        db_table = "sms"