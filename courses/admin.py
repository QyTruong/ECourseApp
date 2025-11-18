from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Course, Lesson
from django import forms
from django.template.response import TemplateResponse
from django.db.models import Count
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'active']
    search_fields = ['name']
    list_filter = ['id', 'name', 'created_date']
    readonly_fields = ['view_image']

    def view_image(self, course):
        return mark_safe(f"<img src='static/{course.image.name}' width='120' />")

    class Media:
        css = {
            'all' : ('static/css/styles.css', )
        }

class LessonAdmin(admin.ModelAdmin):
    form = LessonForm

class MyAdminSite(admin.AdminSite):
    site_header = "eCourse Online"

    def get_urls(self):
        return [path('course-stats/', self.stats_view)] + super().get_urls()

    def stats_view(self, request):
        stats = Category.objects.annotate(count=Count("course")).values('id', 'name', 'count')
        return TemplateResponse(request, 'admin/stats.html', {'stats':stats})

admin_site = MyAdminSite(name="eCourse")

admin_site.register(Category)
admin_site.register(Course, CourseAdmin)
admin_site.register(Lesson, LessonAdmin)
# Register your models here.
