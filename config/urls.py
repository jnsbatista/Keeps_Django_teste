from django.contrib import admin
from django.urls import path, include
from elearning.views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Keeps elarning solution API",
      default_version='v1',
      description="API para solução em elarning",
      terms_of_service="#",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'students', StudentsViewSet, basename='Students')
router.register(r'courses', CoursesViewSet, basename='Courses')
router.register(r'enrollments', EnrollmentsViewSet, basename='Enrollments')
# router.register(r'enrollmentsfullinfo', EnrollmentFullInfoViewSet, basename='EnrollmentFullInfoViewSet')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('student/<int:pk>/enrollments_list/', StudentEnrollmentsList.as_view()),
    path('course/<int:pk>/enrollments_list/', CourseEnrollmentsList.as_view()),
    path('enrollment/disapproved/', DisapprovedEnrollmentsList.as_view()),
    path('enrollment/concluded/', ConcludedEnrollmentsListByDate.as_view()), #/enrollment/concluded/?from_date_close=2022-09-10&to_date_close=2022-10-10
    path('enrollment/started/', StartedEnrollmentsListByDate.as_view()), #/enrollment/started/?from_date_close=2022-09-10&to_date_close=2022-10-10
    path('student/started/', StartedStudentListByDate.as_view()), #/student/started/?from_date_close=2022-09-10&to_date_close=2022-10-10
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
