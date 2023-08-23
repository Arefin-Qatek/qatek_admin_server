from django.urls import path
from .views import CourseListAPIView, CourseAPIView, WeekAPIView,WeekListAPIView

app_name = 'courses'

urlpatterns = [
    path('api/courses/', CourseAPIView.as_view(), name='course-list'),
    path('api/courses/<int:course_id>/', CourseAPIView.as_view(), name='course-detail'),
    path('api/weeks/', WeekAPIView.as_view(), name='week-list'),
    path('api/weeks/<int:week_id>/', WeekAPIView.as_view(), name='week-detail'),
    path('api/weeks/course/<int:course_id>/', WeekAPIView.as_view(), name='week-by-course'),

    # Public URL pattern
    path('api/course-list/', CourseListAPIView.as_view(), name='course-list-public'),
    path('api/week-list/course/<int:course_id>/', WeekListAPIView.as_view(), name='week-by-course-public'),
]

