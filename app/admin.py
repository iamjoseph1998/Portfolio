from django.contrib import admin

from app.models import About, Certification, Education, Experience, Project, Skill

# Register your models here.
admin.site.register(About)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Certification)
