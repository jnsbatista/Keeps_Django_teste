from rest_framework.test import APITestCase
from elearning.models import *
from django.urls import reverse
from rest_framework import status

class StudentsTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Students-list')
        self.student_1 = Student.objects.create(
            name='Student1', nickname='Student1', phone='48558625865', avatar=None, date_created=None, date_updated=None
        )
        self.student_2 = Student.objects.create(
            name='Student2', nickname='Student2', phone='48558625865', avatar=None, date_created=None, date_updated=None
        )

    def test_request_get_all_students_list(self):
        """Teste para verificar requisição GET para listar todos os estudantes"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_post_create_student(self):
        """Teste para verificar requisição POST para criar estudante"""
        data = {
            'name':'Student3',
            'nickname':'Student3', 
            'phone':'48558625865', 
            'avatar':None, 
            'date_created':None, 
            'date_updated':None
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        

class CoursesTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Courses-list')
        self.course_1 = Course.objects.create(
            name='CURSO 1', description='DESCRIÇÃO DO CURSO 1', holder_image=None, duration=2, date_created=None, date_updated=None
        )
        self.course_2 = Course.objects.create(
            name='CURSO 2', description='DESCRIÇÃO DO CURSO 2', holder_image=None, duration=2, date_created=None, date_updated=None
        )
    
    def test_request_get_all_courses_list(self):
        """Teste para verificar requisição GET para listar todos os cursos"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_post_create_course(self):
        """Teste para verificar requisição POST para criar curso"""
        data = {
            'name':'CURSO 3', 
            'description':'DESCRIÇÃO DO CURSO 3', 
            'holder_image':None, 
            'duration':2, 
            'date_created':None, 
            'date_updated':None
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
        
class EnrollmentsTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Enrollments-list')

        self.student_1 = Student.objects.create(
            name='Student1', nickname='Student1', phone='48558625865', avatar=None, date_created=None, date_updated=None
        )
        self.student_2 = Student.objects.create(
            name='Student2', nickname='Student2', phone='48558625865', avatar=None, date_created=None, date_updated=None
        )
        self.student_3 = Student.objects.create(
            name='Student3', nickname='Student3', phone='48558625865', avatar=None, date_created=None, date_updated=None
        )

        self.course_1 = Course.objects.create(
            name='CURSO 1', description='DESCRIÇÃO DO CURSO 1', holder_image=None, duration=2, date_created=None, date_updated=None
        )
        self.course_2 = Course.objects.create(
            name='CURSO 2', description='DESCRIÇÃO DO CURSO 2', holder_image=None, duration=2, date_created=None, date_updated=None
        )
        self.course_3 = Course.objects.create(
            name='CURSO 3', description='DESCRIÇÃO DO CURSO 3', holder_image=None, duration=2, date_created=None, date_updated=None
        )

        self.enrollment_1 = Enrollment.objects.create(
            student=self.student_1, course=self.course_1, date_enroll=None, date_close=None, score=None, status='C', justification=None
        )
        self.enrollment_2 = Enrollment.objects.create(
           student=self.student_2, course=self.course_2, date_enroll=None, date_close=None, score=None, status='C', justification=None
        )
    
    def test_request_get_all_enrollments_list(self):
        """Teste para verificar requisição GET para listar todas as matricular"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_post_create_enrollment(self):
        """Teste para verificar requisição POST para criar matricula"""
        print(self.student_3)
        print(self.course_3)
        data = {
            'student':self.student_3, 
            'course':self.course_3, 
            'date_enroll':None, 
            'date_close':None, 
            'score':None, 
            'status':'C', 
            'justification':None
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)