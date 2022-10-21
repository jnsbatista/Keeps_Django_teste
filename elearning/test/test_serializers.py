from django.test import TestCase
from elearning.models import *
from elearning.serializer import *

class StudentSerializerTestCase(TestCase):
    def setUp(self):        
        self.Student = Student(
            name='Student1', nickname='Student1', phone='48558625865', avatar=None, date_created=None, date_updated=None
        )
        self.serializer = StudentSerializer(instance=self.Student)

    def test_verif_campos_serializados(self):
        """Teste para verificar os campos de estudante que estão serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'nickname', 'phone', 'avatar', 'date_created', 'date_updated']))


class CourseSerializerTestCase(TestCase):
    def setUp(self):        
        self.Course = Course(
            name='CURSO 1', description='DESCRIÇÃO DO CURSO 1', holder_image=None, duration=2, date_created=None, date_updated=None
        )
        self.serializer = CourseSerializer(instance=self.Course)

    def test_verif_campos_serializados(self):
        """Teste para verificar os campos de cusrso que estão serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'description', 'holder_image', 'duration', 'date_created', 'date_updated']))


class EnrollmentSerializerTestCase(TestCase):
    def setUp(self):  
        self.Student = Student(
            name='Student1', nickname='Student1', phone='48558625865', avatar=None, date_created=None, date_updated=None
        )
        self.Course = Course(
                    name='CURSO 1', description='DESCRIÇÃO DO CURSO 1', holder_image=None, duration=2, date_created=None, date_updated=None
                )                    
        self.Enrollment = Enrollment(
            student=self.Student, course=self.Course, date_enroll=None, date_close=None, score=None, status='C', justification=None
        )
        self.serializer = EnrollmentSerializer(instance=self.Enrollment)

    def test_verif_campos_serializados(self):
        """Teste para verificar os campos de matricula que estão serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'student', 'course', 'date_enroll', 'date_close', 'score', 'status', 'justification']))