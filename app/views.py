from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'app/about.html')

def experience(request):
    return render(request, 'app/experience.html')

def education(request):
    return render(request, 'app/education.html')

def skills(request):
    return render(request, 'app/skills.html')

def projects(request):
    return render(request, 'app/projects.html')

def certifications(request):
    return render(request, 'app/certifications.html')