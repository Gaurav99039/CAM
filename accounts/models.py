from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    grade = models.JSONField(null=True,default=dict)
    extracurriculars = models.JSONField(default=list)
    no_of_subject = models.PositiveIntegerField(null=True)
        


    def __str__(self):
        return f"{self.first_name} {self.last_name}"