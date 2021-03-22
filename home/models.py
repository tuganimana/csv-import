from django.db import models

# Create your models here.

class Uploadcsv(models.Model):
    firstname =models.CharField(max_length=255, default="")
    email =models.CharField(max_length=255, default="")
    address =models.CharField(max_length=255, default="")
    def __str__(self):
        return self.firstname