from django.urls import path
from .views import home, course_view

app_name = 'courses'

urlpatterns = [path('', home, name='home'),
               path('<str:category>/<str:course>/', course_view, name='course'),
                path('<str:category>/<str:course>/<str:link>/', course_view, name='course_videos'),

               ]
