from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    TYPE_CHOICES = (
        ('Employer', 'Employer'),
        ('Employee', 'Employee')
    )
    type = models.CharField(max_length=120, choices=TYPE_CHOICES)
    company = models.ForeignKey("Company", on_delete=models.SET_NULL, null=True)


class Company(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="owner")
    name = models.CharField(max_length=120)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)


class Branch(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    worker = models.ManyToManyField(User)
    date = models.DateField(auto_now_add=True)


class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    workers = models.ManyToManyField(User)
    date = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True)
