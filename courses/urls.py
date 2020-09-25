from django.urls import path
from .views import home, sample, course_view

app_name = 'courses'

urlpatterns = [path('', home, name='home'),
               path('sample/', sample, name='sample'),
               path('<slug:category>/<slug:course>', course_view, name='course'),
               ]
