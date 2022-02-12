from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'app/about.html')

def experience(request):
    return render(request, 'app/experience.html')