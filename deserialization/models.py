from django.db import models

from django.db import models

class Student(models.Model):

    name = models.CharField(max_length= 111)
    roll = models.IntegerField()
    city = models.CharField(max_length = 111)

    def __str__(self):
        return self.name
