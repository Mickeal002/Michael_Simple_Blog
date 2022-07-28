from django.db import models
from datetime import datetime

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=90)
    body = models.CharField(max_length=12000000)
    uploaded_at = models.DateTimeField(default=datetime.now, blank=True)
