from django.db import models

# Create your models here.
class Url(models.Model):
    link = models.CharField(max_length=10000)
    #a uid will be assigned to the link inputted by the user
    uuid = models.CharField(max_length=10)
