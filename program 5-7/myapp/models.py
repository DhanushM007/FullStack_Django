

# Create your models here.
from django.db import models
from django.forms import ModelForm
class course(models.Model):
    course_code=models.CharField(max_length=40)
    course_name=models.CharField(max_length=100)
    course_credits=models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.course_name
    
class student(models.Model):
    student_usn=models.CharField(max_length=20)
    student_name=models.CharField(max_length=100)
    student_sem=models.IntegerField()
    enrolment=models.ManyToManyField(course)
    def __str__(self):
        return self.student_name+"("+self.student_usn+")"
    


class Project(models.Model): 
    studentname= models.CharField(max_length=200) 
    ptopic=models.CharField(max_length=200) 
    plangauges=models.CharField(max_length=200) 
    pduration=models.IntegerField()
