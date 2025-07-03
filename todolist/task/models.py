from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):

    title = models.CharField(max_length=100)
    text =  models.TextField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title
    