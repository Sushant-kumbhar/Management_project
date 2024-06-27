# management_application/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_clients')

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.name
