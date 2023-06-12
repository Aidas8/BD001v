from django.db import models

# Create your models here.
class Darbuotojai1(models.Model):
    vardas = models.CharField(max_length=255)
    pavarde = models.CharField(max_length=255)
    telefonas = models.IntegerField(blank=False, null=False)
    epastas = models.CharField(max_length=255)

