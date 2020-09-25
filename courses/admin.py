from django.contrib import admin
from .models import CourseCatalogue, Courses, CourseContentHeadings, CourseContentVideos

# Register your models here.

admin.site.register(CourseCatalogue)
admin.site.register(Courses)

admin.site.register(CourseContentHeadings)
admin.site.register(CourseContentVideos)
