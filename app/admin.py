from django.contrib import admin

from app.models import About, Certification, Education, Experience, Project, Skill

# AboutAdmin
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'mobile', 'email', 'address')
    list_display_links = ('id', 'first_name', 'last_name')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False



# ExperienceAdmin
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('designation', 'company_name', 'current_working', 'joined')



# EducationAdmin
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree_name', 'university', 'percentage', 'start_year', 'end_year', 'current_pursuing')

    def render_change_form(self, request, context, *args, **kwargs):
        form_instance = context['adminform'].form
        form_instance.fields['degree_name'].widget.attrs['placeholder'] = 'Master\'s in Computer Science'
        form_instance.fields['university'].widget.attrs['placeholder'] = 'Savitribai Phule Pune Unversity'
        form_instance.fields['percentage'].widget.attrs['placeholder'] = '99.9'
        form_instance.fields['start_date'].widget.attrs['placeholder'] = 'yyyy-mm-dd'
        form_instance.fields['end_date'].widget.attrs['placeholder'] = 'yyyy-mm-dd'
        return super().render_change_form(request, context, *args, **kwargs)

admin.site.register(Skill)



# ProjectAdmin
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'proj_github_link', 'currently_working')
    list_display_links = ('id', 'project_name')



# CertificationAdmin
@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'certificate_name')
    list_display_links = ('id', 'certificate_name')
