from django.contrib import admin

from app.models import About, Certification, Education, Experience, Project, Skill

# Register your models here.
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'mobile', 'email', 'address')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Experience)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree_name', 'university', 'percentage', 'current_pursuing', 'start_year', 'end_year')

    def render_change_form(self, request, context, *args, **kwargs):
        form_instance = context['adminform'].form
        form_instance.fields['degree_name'].widget.attrs['placeholder'] = 'Master\'s in Computer Science'
        form_instance.fields['university'].widget.attrs['placeholder'] = 'Savitribai Phule Pune Unversity'
        form_instance.fields['percentage'].widget.attrs['placeholder'] = '99.9'
        form_instance.fields['start_date'].widget.attrs['placeholder'] = 'yyyy-mm-dd'
        form_instance.fields['end_date'].widget.attrs['placeholder'] = 'yyyy-mm-dd'
        return super().render_change_form(request, context, *args, **kwargs)

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Certification)
