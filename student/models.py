from django.db import models

# Create your models here.

class Student(models.Model):
    student_code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)
    marjo = models.CharField(max_length=200)