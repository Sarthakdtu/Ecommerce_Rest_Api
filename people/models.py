from django.db import models
from django.utils import timezone
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(default=timezone.now)
    