from django.db import models

# Create your models here.


class Create(models.Model):
    data = models.TextField(max_length=250)
    name = models.CharField(max_length=50)

