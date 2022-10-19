from django import views
from django.contrib import admin
from django.urls import path, include
from elearning.views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'students', StudentsViewSet, basename='Students')
router.register(r'courses', CoursesViewSet, basename='Courses')
router.register(r'enrollments', EnrollmentsViewSet, basename='Enrollments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('student/<int:pk>/enrollments_list/', StudentEnrollmentsList.as_view()),
    path('course/<int:pk>/enrollments_list/', CourseEnrollmentsList.as_view()),
    path('enrollment/disapproved/', DisapprovedEnrollmentsList.as_view()),
    path('enrollment/concluded/', ConcludedEnrollmentsListByDate.as_view()), #/enrollment/concluded/?from_date_close=2022-09-10&to_date_close=2022-10-10
    path('enrollment/started/', StartedEnrollmentsListByDate.as_view()), #/enrollment/started/?from_date_close=2022-09-10&to_date_close=2022-10-10
    path('student/started/', StartedEnrollmentsListByDate.as_view()), #/student/started/?from_date_close=2022-09-10&to_date_close=2022-10-10
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
