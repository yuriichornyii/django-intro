from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class WishList(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    wish = models.CharField(max_length=255)