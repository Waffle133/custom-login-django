from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from categories.models import Categories
from products.validators import validate_sku


class Products(models.Model):
    name = models.CharField(
        max_length=150,
    )
    sku = models.CharField(
        max_length=10,
        unique=True,
        error_messages={
            'unique': "El producto con este SKU ya existe",
        },
        validators=[validate_sku]
    )
    description = models.TextField(
        blank=True,
        null=True
    )

    show = models.BooleanField(
        default=True,
    )

    categories = models.ManyToManyField(Categories)

    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
