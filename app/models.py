from datetime import datetime
from enum import unique
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError

# Create your models here.
class About(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    mobile = PhoneNumberField(unique=True, max_length=13)
    email = models.EmailField(max_length=70, unique=True)
    address = models.CharField(max_length=150)
    github_link = models.CharField(max_length=150)
    linkedin_link = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def clean(self):
        if (About.objects.count() >= 1 and self.pk is None):
            raise ValidationError("Can only create one Profile instances. Try editing/removing one of the existing instances.")

class Experience(models.Model):
    designation = models.CharField(max_length=100)
    company_name = models.CharField(max_length=150)
    current_working = models.BooleanField(default=False)
    join_date = models.DateField(unique=True)
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.designation} at {self.company_name}'
    
    def joined(self):
        return self.join_date.strftime('%b, %Y')

    def resigned(self):
        return self.end_date.strftime('%b, %Y')

class Education(models.Model):
    degree_name = models.CharField(max_length=200, unique=True)
    university = models.CharField(max_length=200)
    percentage = models.FloatField()
    current_pursuing = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.degree_name}'

    def start_year(self):
        return self.start_date.strftime('%Y')

    def end_year(self):
        return self.end_date.strftime('%Y')

class Skill(models.Model):
    cat_choices = (
        ("Programming Languages", "Programming Languages"),
        ("Frameworks", "Frameworks"),
        ("Frontend Technology", "Frontend Technology"),
        ("Database Technology", "Database Technology"),
        ("Source Control", "Source Control"),
    )
    category = models.CharField(max_length=50, choices=cat_choices)
    skill = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.skill}'

class Project(models.Model):
    project_name = models.CharField(max_length=150)
    proj_github_link = models.CharField(max_length=200, unique=True, blank=True, null=True)
    tech_used = models.TextField()
    description = models.TextField()
    currently_working = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.project_name}'

class Certification(models.Model):
    certificate_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.certificate_name}'