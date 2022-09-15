from asyncio import Task
from email.policy import default
from multiprocessing.dummy import Manager
from pyexpat import model
from tkinter.tix import Select
from turtle import done
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskList(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task + " - " + str(self.done)
