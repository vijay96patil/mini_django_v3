from django.db import models


# Create your models here.


class Mymodel(models.Model):
    field1 = models.CharField(max_length=250)
    field2 = models.CharField(max_length=250)
