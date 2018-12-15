from django.db import models

# Create your models here.


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField()
    email = models.CharField(max_length=100)
    size = models.CharField(max_length=5)
