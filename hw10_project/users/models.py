from django.db import models
class Picture(models.Model):
    description = models.CharField(max_length=150)
