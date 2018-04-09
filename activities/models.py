from django.db import models

import datetime
from django.utils import timezone

# Create your models here.

class Schedule(models.Model):
    description = models.CharField(max_length=100)
    date_begin = models.DateTimeField('date of beginning')
    date_end = models.DateTimeField('date of closing')

    def __str__(self):
        return self.description

    def is_open(self):
        return (timezone.now() >= self.date_begin and timezone.now() <= self.date_end) 

    def ordered_action_set(self):
        return self.action_set.all().order_by('-priority')

    is_open.short_description = 'Is really opened?'


class Action(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    priority = models.IntegerField(default=0)
    closed = models.BooleanField(default=False)
    finish = models.BooleanField(default=False)
    notes = models.CharField(max_length=300,blank=True)

    def __str__(self):
        return self.description

