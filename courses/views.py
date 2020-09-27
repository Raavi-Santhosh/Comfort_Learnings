from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import CourseCatalogue, CourseContentHeadings, CourseContentVideos, Courses


def home(request):
    return render(request, 'index.html')


def course_view(request, category, course, link=None):

    context = dict()

    try:
        target_course = Courses.objects.get(course_category__category_name_slug__exact=category,
                                            course_category__is_active=True,
                                            course_name_slug__exact=course, is_active=True)
    except Courses.DoesNotExist:
        raise Http404("The page you are looking for does not exists")

    context['course'] = target_course
    course_headings = target_course.course_content_heading.all().filter(is_active=True)

    if not course_headings:
        return render(request, 'coming-soon.html')

    context['course_headings'] = course_headings

    if link and link != 'no-link':
        try:
            context['link'] = target_course.course_content_videos.get(video_uid__exact=link).video_link
        except target_course.DoesNotExist:
            raise Http404("The video you are looking for does not exists")
    else:
        context['link'] = target_course.course_content_videos.all()[0].video_link

    return render(request, 'courses/courses.html', context=context)



