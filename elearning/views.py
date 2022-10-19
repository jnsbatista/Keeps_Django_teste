from urllib import request, response
from rest_framework import viewsets, generics, filters
from elearning.models import *
from elearning.serializer import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class EnrollmentsViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    filter_backends = [DjangoFilterBackend]
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class StudentEnrollmentsList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = StudentEnrollmentsListSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class CourseEnrollmentsList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = CourseEnrollmentsListSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class DisapprovedEnrollmentsList(generics.ListAPIView):
    def get_queryset(self):
        status_r = "R"
        queryset = Enrollment.objects.filter(status=status_r)
        return queryset
    serializer_class = DisapprovedEnrollmentsListSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class ConcludedEnrollmentsListByDate(generics.ListAPIView):
    def get_queryset(self):
        from_date_close = self.request.GET.get('from_date_close')
        to_date_close = self.request.GET.get('to_date_close')        
        queryset = Enrollment.objects.filter(date_close__range=(from_date_close, to_date_close))   
        return queryset
    serializer_class = ConcludedEnrollmentsListByDateSerializer

class StartedEnrollmentsListByDate(ListAPIView):
    def get_queryset(self):
        from_date_close = self.request.GET.get('from_date_close')
        to_date_close = self.request.GET.get('to_date_close')        
        queryset = Enrollment.objects.filter(date_enroll__range=(from_date_close, to_date_close))   
        return queryset
    serializer_class = StartedEnrollmentsListByDateSerializer

class StartedStudentListByDate(ListAPIView):
    def get_queryset(self):
        from_date_close = self.request.GET.get('from_date_close')
        to_date_close = self.request.GET.get('to_date_close')        
        queryset = Enrollment.objects.filter(date_created__range=(from_date_close, to_date_close))   
        return queryset
    serializer_class = StartedStudentListByDateSerializer