from enum import unique
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class About(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile = PhoneNumberField(unique=True, max_length=12)
    email = models.EmailField(max_length=70, unique=True)
    address = models.CharField(max_length=150)
    github_link = models.CharField(max_length=150)
    linkedin_link = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Experience(models.Model):
    designation = models.CharField(max_length=100)
    company_name = models.CharField(max_length=150)
    current_working = models.BooleanField(default=False)
    join_date = models.DateField(unique=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.designation} at {self.company_name}'

class Education(models.Model):
    degree_name = models.CharField(max_length=200, unique=True)
    university = models.CharField(max_length=200)
    percentage = models.FloatField()
    current_pursuing = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.degree_name}'

class Skill(models.Model):
    category = models.CharField(max_length=50)
    skill = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.skill}'

class Project(models.Model):
    project_name = models.CharField(max_length=150)
    proj_github_link = models.CharField(max_length=200, unique=True)
    tech_used = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'{self.project_name}'

class Certification(models.Model):
    certi_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.certi_name}'