from unicodedata import name
from django.shortcuts import render
from . import models

# Create your views here.
def about(request):

    about_data = models.About.objects.get(id=1)

    context = {'about_data': about_data}

    return render(request, 'app/about.html', context=context)

def experience(request):

    about_data = models.About.objects.get(id=1)

    context = {'about_data': about_data}

    return render(request, 'app/experience.html', context=context)

def education(request):

    about_data = models.About.objects.get(id=1)

    edu_data = models.Education.objects.all()

    context = {'about_data': about_data, 'edu_data': edu_data}

    return render(request, 'app/education.html', context=context)

def skills(request):

    about_data = models.About.objects.get(id=1)

    context = {'about_data': about_data}

    return render(request, 'app/skills.html', context=context)

def projects(request):

    about_data = models.About.objects.get(id=1)

    context = {'about_data': about_data}

    return render(request, 'app/projects.html', context=context)

def certifications(request):

    about_data = models.About.objects.get(id=1)

    context = {'about_data': about_data}

    return render(request, 'app/certifications.html', context=context)