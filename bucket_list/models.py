from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class To_do(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Task = models.CharField(max_length=200, null=True)
    Time_required = models.CharField(max_length=200, null=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True, blank=True)



    def __str__(self):
        return self.Task

    class Meta:
        ordering = ['complete']


