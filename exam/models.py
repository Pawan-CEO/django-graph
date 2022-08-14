from django.db import models

# Create your models here.

class Exams(models.Model):
    rno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.FloatField()
    
    def __str__(self):
        return self.ename