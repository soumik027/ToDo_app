from django.db import models

# Create your models here.
class Task(models.Model):
    task=models.CharField(max_length=250)
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    session_key= models.CharField(max_length=40, blank=True, null=True)  
    def __str__(self):
        return self.task
    