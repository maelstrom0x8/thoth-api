from django.db import models
import uuid


class LogEntry(models.Model):
    class Meta:
        ordering = ['created']

    log_id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False)
    subject = models.CharField(max_length=200, blank=True)
    body = models.TextField(max_length=100000)
    created = models.DateTimeField(auto_now_add=True)
