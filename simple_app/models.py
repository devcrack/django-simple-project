from django.db import models

# Create your models here.


class SimpleInfo(models.Model):
    name = models.CharField(null=False, blank=False, max_length=256)
    address = models.CharField(null=False, blank=False, max_length=256)
    number_phone = models.CharField(null=False, blank=False, max_length=256)