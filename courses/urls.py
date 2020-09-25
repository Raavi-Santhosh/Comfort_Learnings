from django.urls import path
from .views import home, course_view, sample

app_name = 'courses'

urlpatterns = [path('', home, name='home'),
               path('<slug:category>/<slug:course>', course_view, name='course'),
               path('courses/', sample, name='courses'),
               ]
