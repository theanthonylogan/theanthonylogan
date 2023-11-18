from django.db import models
from datetime import datetime

from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    description = models.CharField(max_length=255)
    notes = models.TextField()
    completed = models.BooleanField()
    due_date = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
