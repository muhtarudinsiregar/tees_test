from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    size = models.CharField(max_length=5)
    user = models.ForeignKey(
        User, related_name='order', on_delete=models.CASCADE)


class Meta:
    ordering = ('created',)
