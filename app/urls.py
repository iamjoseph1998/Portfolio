from django.urls import path
from . import views

#register app for urls tag
app_name = 'app'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('experience/', views.experience, name='experience'),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
]
