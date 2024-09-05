from django.db import models

# Create your models here.
class Timetable_IOTCSBT(models.Model):
    day = models.CharField(max_length=100)
    period1 = models.CharField(max_length=100)
    period2 = models.CharField(max_length=100)
    period3 = models.CharField(max_length=100)
    period4 = models.CharField(max_length=100)
    period5 = models.CharField(max_length=100)
    period6 = models.CharField(max_length=100)
    period7 = models.CharField(max_length=100, default='null')

class Timetable_IOT(models.Model):
    day = models.CharField(max_length=100)
    period1 = models.CharField(max_length=100)
    period2 = models.CharField(max_length=100)
    period3 = models.CharField(max_length=100)
    period4 = models.CharField(max_length=100)
    period5 = models.CharField(max_length=100)
    period6 = models.CharField(max_length=100)
    period7 = models.CharField(max_length=100)

class Timetable_IT(models.Model):
    day = models.CharField(max_length=100)
    period1 = models.CharField(max_length=100)
    period2 = models.CharField(max_length=100)
    period3 = models.CharField(max_length=100)
    period4 = models.CharField(max_length=100)
    period5 = models.CharField(max_length=100)
    period6 = models.CharField(max_length=100)
    period7 = models.CharField(max_length=100)