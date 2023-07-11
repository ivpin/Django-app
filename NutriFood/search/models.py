from django.db import models

# Create your models here.
class produit(models.Model):
    ingrédient = models.CharField(max_length=200)