from unicodedata import name
from django.shortcuts import render
from . import models
import datetime


# About
def about(request):

    about_data = models.About.objects.get(id=1)

    context = {'about_data': about_data}

    return render(request, 'app/about.html', context=context)



# Experience
def experience(request):

    about_data = models.About.objects.all()
    exp_data = models.Experience.objects.order_by('-end_date')

    context = {'about_data': about_data, 'exp_data': exp_data}

    return render(request, 'app/experience.html', context=context)



# Education
def education(request):

    about_data = models.About.objects.get(id=1)

    edu_data = models.Education.objects.order_by('-end_date')

    context = {'about_data': about_data, 'edu_data': edu_data,}

    return render(request, 'app/education.html', context=context)



# Skills
def skills(request):

    about_data = models.About.objects.get(id=1)

    context = {'about_data': about_data}

    return render(request, 'app/skills.html', context=context)



# Projects
def projects(request):

    about_data = models.About.objects.get(id=1)

    context = {'about_data': about_data}

    return render(request, 'app/projects.html', context=context)




# Certifications
def certifications(request):

    about_data = models.About.objects.get(id=1)
    cert_data = models.Certification.objects.all()

    context = {'about_data': about_data, 'cert_data': cert_data}

    return render(request, 'app/certifications.html', context=context)