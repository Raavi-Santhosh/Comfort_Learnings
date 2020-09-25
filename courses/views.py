from django.shortcuts import render
from .models import CourseCatalogue


def home(request):
    category = CourseCatalogue.objects.filter(is_active=True)
    return render(request, 'index.html', context={'category': category, })


def course_view(request):
    pass

def sample(request):
    return render(request, 'courses/courses.html')
