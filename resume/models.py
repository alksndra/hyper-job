from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

