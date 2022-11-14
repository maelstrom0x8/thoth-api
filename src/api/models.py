
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class LogEntry(models.Model):
    class Meta:
        ordering = ['created']

    log_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=200, blank=True)
    body = models.TextField(max_length=100000)
    created = models.DateTimeField(auto_now_add=True)
