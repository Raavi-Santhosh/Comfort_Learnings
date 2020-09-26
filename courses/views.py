from django.shortcuts import render
from django.http import Http404
from .models import CourseCatalogue, CourseContentHeadings, CourseContentVideos, Courses


def home(request):
    category = CourseCatalogue.objects.filter(is_active=True)
    return render(request, 'index.html', context={'category': category, })


def course_view(request, category, course):
    context = dict()

    try:
        target_course = Courses.objects.get(course_category__category_name_slug=category, course_category__is_active=True,
                                            course_name_slug=course, is_active=True)
    except Courses.DoesNotExist:
        raise Http404("The page you are looking for does not exists")

    context['course_title'] = target_course.course_name
    context['course_headings'] = target_course.course_content_heading.all().filter(is_active=True)

    return render(request, 'courses/courses.html', context=context)


def sample(request):
    return render(request, 'courses/courses.html')
