# models.py
from django.db import models


class RegisteredUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    course = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.username} - {self.course}"

