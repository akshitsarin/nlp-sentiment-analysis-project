from django.db import models

class Reviews(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=100)
    positive = models.IntegerField()
    negative = models.IntegerField()