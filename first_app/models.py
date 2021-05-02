from django.db import models
from datetime import datetime

# Create your models here.
class Asset(models.Model):
    assetid = models.CharField(max_length=50,blank=False)
    name = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.assetid

class Worker(models.Model):
    workerid = models.CharField(max_length=50,blank=False)
    name = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.name

class Task(models.Model):
    FREQ_CHOICES = [               #List of tuple to provide specific choices in 'classno' field.
        ('hourly','hourly'),
        ('daily','daily'),
        ('weekly','weekly'),
        ('monthly','monthly'),
        ('yearly','yearly')
    ]
    taskid = models.CharField(max_length=50,blank=False)
    name = models.CharField(max_length=100,blank=False)
    assetid = models.ForeignKey(Asset, blank = False, on_delete = models.CASCADE)
    workerid = models.ForeignKey(Worker, null = True, on_delete = models.SET_NULL)
    timeOfAllocation = models.DateTimeField(default = datetime.now(), blank=True)
    taskToBePerformedBy = models.DateTimeField(default = datetime.now(), blank=True)
    frequency = models.CharField(max_length=50,
    choices = FREQ_CHOICES,
    default = 'hourly')

    def __str__(self):
        return self.name
