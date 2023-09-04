from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank=True)
    title = models.CharField(max_length=200)
    # completiondate = models.DateField(default=datetime.date.today)
    # remainingdays = completiondate - datetime.date.today()
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateField( auto_now_add=True)

    def __str__(self):
        return self.title
    
    # def calcdate():
    #     remainingdays = completiondate - datetime.date.today() 

    class Meta:
        ordering = ['complete']
