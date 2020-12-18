from django.db import models
from django.utils import timezone


class Categories(models.Model):
    name = models.CharField(
        max_length=150
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name