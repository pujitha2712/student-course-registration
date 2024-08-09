from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrolled_courses = models.ManyToManyField('Course', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.course_name} ({self.course_code})'
