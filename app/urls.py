from django.urls import path
from . import views

#register app for urls tag
app_name = 'app'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('experience/', views.experience, name='experience'),
]
