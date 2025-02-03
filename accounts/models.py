from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    grade = models.JSONField(null=True,default=dict,blank=True)
    extracurriculars = models.JSONField(default=list,blank=True)
    no_of_subject = models.PositiveIntegerField(null=True)
    graduation_year = models.PositiveIntegerField(null=True)
    profile_pic = models.ImageField(null=True,blank=True)

    application_status = models.CharField(
    max_length=20,
    choices=[
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Submitted', 'Submitted'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected')
    ],
    default='Not Started'
)
    note = models.TextField(max_length=300,null=True,blank=True)
        


    def __str__(self):
        return f"{self.first_name} {self.last_name}"