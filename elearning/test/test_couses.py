from rest_framework.test import APITestCase
from elearning.models import *
from django.urls import reverse
from rest_framework import status

from elearning.serializer import CourseSerializer

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
        # get data from db
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_request_post_create_course(self):
        """Teste para verificar requisição POST para criar curso"""
        data = {
            'name':'CURSO 3', 
            'description':'DESCRIÇÃO DO CURSO 3', 
            'holder_image':None, 
            'duration':2, 
            'date_created':"2022-10-19", 
            'date_updated':None
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_request_delete_course(self):
        """Teste para verificar requisição DELETE curso"""
        url = reverse('Courses-detail', kwargs={'pk': self.course_1.pk})
        response = self.client.delete(url)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_request_put_update_course(self):
        """Teste para verificar requisição PUT para atualizar um curso"""
        data = {
            'name':'CURSO 2', 
            'description':'DESCRIÇÃO DO CURSO 2 ATUALIZADO', 
            'holder_image':None, 
            'duration':2, 
            'date_created':"2022-10-11", 
            'date_updated':"2022-10-19"
        }
        url = reverse('Courses-detail', kwargs={'pk': self.course_2.pk})
        response = self.client.put(url, data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)