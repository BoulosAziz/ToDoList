from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task_name
    