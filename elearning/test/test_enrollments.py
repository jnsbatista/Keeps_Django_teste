from asyncio.windows_events import NULL
from rest_framework.test import APITestCase
from elearning.models import *
from django.urls import reverse
from rest_framework import status

class EnrollmentsTestCase(APITestCase):

    def setUp(self):
        """Setando os dados"""
        self.list_url = reverse('Enrollments-list')
        
        self.student_1 = Student.objects.create(
            name='Student1', nickname='Student1', phone='48558625865', avatar=None, date_created="2022-10-13", date_updated=None
        )
        self.student_2 = Student.objects.create(
            name='Student2', nickname='Student2', phone='48558625865', avatar=None, date_created="2022-9-13", date_updated=None
        )
        self.student_3 = Student.objects.create(
            name='Student3', nickname='Student3', phone='48558625865', avatar=None, date_created="2022-9-13", date_updated=None
        )

        self.course_1 = Course.objects.create(
            name='CURSO 1', description='DESCRIÇÃO DO CURSO 1', holder_image=None, duration=2, date_created="2022-10-13", date_updated=None
        )
        self.course_2 = Course.objects.create(
            name='CURSO 2', description='DESCRIÇÃO DO CURSO 2', holder_image=None, duration=2, date_created="2022-9-13", date_updated=None
        )
        self.course_3 = Course.objects.create(
            name='CURSO 3', description='DESCRIÇÃO DO CURSO 3', holder_image=None, duration=2, date_created="2022-9-13", date_updated=None
        )

        self.enrollment_1 = Enrollment.objects.create(
            student=self.student_1, course=self.course_1, date_enroll="2022-10-13", date_close=None, score=None, status='C', justification=None
        )
        self.enrollment_2 = Enrollment.objects.create(
           student=self.student_2, course=self.course_2, date_enroll="2022-9-13", date_close=None, score=None, status='C', justification=None
        )
    
    def test_request_get_all_enrollments_list(self):
        """Teste para verificar requisição GET para listar todas as matricular"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_request_post_create_enrollment(self):
        """Teste para verificar requisição POST para criar matricula"""           
        data = {
        'student':self.student_3.pk, 
        'course':self.course_3.pk, 
        'date_enroll':"2022-10-14", 
        'date_close':None, 
        'score':"0", 
        'status':'C', 
        'justification':NULL
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_request_delete_enrollment(self):
        """Teste para verificar requisição DELETE matricula"""
        url = reverse('Enrollments-detail', kwargs={'pk': self.enrollment_1.pk})
        print(self.client.get(url))
        response = self.client.delete(url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_request_patch_update_enrollment(self):
        """Teste para verificar requisição PUT para atualizar uma matricula"""
        data = {
            'student':self.student_2.pk, 
            'course':self.course_2.pk, 
            'date_enroll':"2022-10-11", 
            'date_close':"2022-10-20", 
            'score':"6", 
            'status':'A', 
            'justification':NULL
        }
        
        url = reverse('Enrollments-detail', kwargs={'pk': self.enrollment_2.pk})
        response = self.client.patch(url, data=data, format="json")
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    
    def test_request_get_all_enrollments_by_date(self):
        """Teste para verificar requisição GET por data de matricula"""
        url = "/enrollment/started/?from_date_close=2022-09-10&to_date_close=2023-10-10"
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    
    def test_request_get_all_enrollments_by_close_date(self):
        """Teste para verificar requisição GET por data de termino"""
        url = "/enrollment/started/?from_date_close=2022-09-10&to_date_close=2022-10-10"
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    
    def test_request_get_all_enrollments_disapproved(self):
        """Teste para verificar requisição GET por data de termino"""
        url = "enrollment/disapproved/"
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)