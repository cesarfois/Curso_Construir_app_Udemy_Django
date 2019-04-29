from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Registrado(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.email
