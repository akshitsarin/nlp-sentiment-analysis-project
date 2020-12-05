from django.db import models

class Reviews(models.Model):
    name = models.CharField(max_length=100)
    positive = models.IntegerField()
    negative = models.IntegerField()