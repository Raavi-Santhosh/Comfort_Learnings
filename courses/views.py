from django.shortcuts import render
from .models import CourseCatalogue, CourseContentHeadings, CourseContentVideos, Courses


def home(request):
    category = CourseCatalogue.objects.filter(is_active=True)
    return render(request, 'index.html', context={'category': category, })


def course_view(request, category, course):
    context = dict()

    category = CourseCatalogue.objects.filter(category_name=category)
    course = Courses.objects.filter(course_name=course)

    CourseContentVideos.objects.filter(course__course_name=course.course_name)

    return render(request, 'courses/courses.html', )


def sample(request):
    return render(request, 'courses/courses.html')
