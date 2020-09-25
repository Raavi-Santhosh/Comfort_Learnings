from django.shortcuts import render
from django.http import HttpResponse

from .models import Courses, CourseCatalogue
# Create your views here.


def home(request):
    return render(request, 'index.html')


def sample(request):
    courses = Courses.objects.filter(is_active=True)
    category = CourseCatalogue.objects.all().filter(is_active=True)

    return render(request, 'sample.html', context={'courses': courses, 'category': category})


def course_view(request, category, course):
    return
