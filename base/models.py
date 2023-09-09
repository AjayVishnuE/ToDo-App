from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import date
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank=True)
    title = models.CharField(max_length=200)
    completiondate = models.DateField(default=datetime.date.today)
    # remainingdays = models.IntegerField()
    # remainingdays = completiondate - datetime.date.today()
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateField( auto_now_add=True, )

    def __str__(self):
        return self.title
    
    @property
    def remaining_days(self):
        remaining = (self.completiontime - datetime.datetime.today()).days
        return remaining
    # def clean(self):
    #     self.remainingdays = (dt.strptime(self.completiondate, "%Y/%m/%d") - dt.strptime(self.create, "%Y/%m/%d")).days
    #     print(self.remainingdays)

    class Meta:
        ordering = ['complete']
