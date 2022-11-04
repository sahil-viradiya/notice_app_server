from django.db import models
from django.db.models import Model


class Event(Model):
    added = models.DateTimeField(auto_now_add=True)
    holiday = models.BooleanField(default=False)
    image = models.URLField(blank=True)
    msg = models.TextField(max_length=5000)
    scheduled_at = models.DateTimeField()

    def __str__(self):
        return self.msg


class Quote(Model):
    author = models.CharField(max_length=500)
    quote = models.CharField(max_length=500)

    def __str__(self):
        return self.author

