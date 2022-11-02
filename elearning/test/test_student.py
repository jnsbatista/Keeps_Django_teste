from django.test import Client, TestCase
from rest_framework.test import APITestCase
from elearning.models import *
from django.urls import reverse
from rest_framework import status
        
class StudentsTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('Students-list')
        self.student_1 = Student.objects.create(
            id=1, name='Student1', nickname='Student1', phone='48558625865', avatar=None, date_created="2022-10-11", date_updated=None
        )
        self.student_2 = Student.objects.create(
            id=2, name='Student2', nickname='Student2', phone='48558625865', avatar=None, date_created="2022-10-11", date_updated=None
        )

    def test_request_get_all_students_list(self):
        """Teste para verificar requisição GET para listar todos os estudantes"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_request_post_create_student(self):
        """Teste para verificar requisição POST para criar estudante"""
        data = {
            'name':'Student3',
            'nickname':'Student3', 
            'phone':'48558625865', 
            'avatar':None, 
            'date_created':"2022-10-19", 
            'date_updated':None
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_request_delete_student(self):
        """Teste para verificar requisição DELETE estudante"""
        url = reverse('Students-detail', kwargs={'pk': self.student_1.pk})
        response = self.client.delete(url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_request_put_update_student(self):
        """Teste para verificar requisição PUT para atualizar um estudante"""
        data = {
            'name':'Student2',
            'nickname':'Student2', 
            'phone':'48000000000', 
            'avatar':None, 
            'date_created':"2022-10-11", 
            'date_updated':None
        }
        url = reverse('Students-detail', kwargs={'pk': self.student_2.pk})
        response = self.client.put(url, data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_request_get_all_students_by_start_date(self):
        """Teste para verificar requisição GET por data de matricula de estudante"""
        url = "/student/started/?from_date_close=2022-09-10&to_date_close=2022-10-20"
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)