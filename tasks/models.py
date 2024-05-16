
from django.db import models
x = [
    ('Low', 'Low'),
    ('High', 'High'),
    ('Medium', 'Medium')
]

class Task(models.Model):
    Taskiid = models.IntegerField(null=True)
    title = models.CharField(max_length=55,null=True)
    teacher = models.CharField(max_length=55,null=True)
    choose = models.CharField(max_length=6, choices=x,null=True)
    Description = models.TextField(max_length=160, blank=True, null=True)
    admin = models.CharField(max_length=15,null=True)
    completed = models.BooleanField(default=False,null=True)

    def __str__(self):
        return self.title




   
