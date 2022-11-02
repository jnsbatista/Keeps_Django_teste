from rest_framework import serializers
from elearning.models import *
from elearning.validators import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'holder_image', 'duration', 'date_created', 'date_updated']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'nickname', 'phone', 'avatar', 'date_created', 'date_updated']

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'date_enroll', 'date_close', 'score', 'status', 'justification']
    def validate(self, data):
        if not reprova_valid(data['score'], data['status']):
            raise serializers.ValidationError({'status':"Para ser aprovado precisa atingir nota igual ou maior que 6"})
        if not aprova_valid(data['score'], data['status']):
            raise serializers.ValidationError({'status':"Se o aluno obtém nota igual ou maior que 6 ele está APROVADO!"})
        if not term_valid(data['date_close'], data['status']):
            raise serializers.ValidationError({'status':"Informe a data em que terminou o curso."})   
        if not quitter_valid(data['status'], data['justification']):
            raise serializers.ValidationError({'student':"Informe a justificativa da desistência"}) 
        if not user_valid_enrollment(data['student']):
            raise serializers.ValidationError({'student':"Usuário já matriculado em um curso"})   
        if not async_keeps_f():
            raise serializers.ValidationError({'student':"KEEEEPPPSSSS"})       
        return data


class StudentEnrollmentsListSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.name')
    status = serializers.SerializerMethodField()
    class Meta:
        model = Enrollment
        exclude = ['id','student', 'date_enroll', 'date_close', 'score']
    def get_status(self, obj):
        return obj.get_status_display()

class CourseEnrollmentsListSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')
    status = serializers.SerializerMethodField()
    class Meta:
        model = Enrollment
        exclude = ['id', 'course', 'date_enroll', 'date_close', 'score']
    def get_status(self, obj):
        return obj.get_status_display()

class DisapprovedEnrollmentsListSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')
    course = serializers.ReadOnlyField(source='course.name')    
    status = serializers.SerializerMethodField()
    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'score', 'status']
    def get_status(self, obj):
        return obj.get_status_display()

class ConcludedEnrollmentsListByDateSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')
    course = serializers.ReadOnlyField(source='course.name')    
    status = serializers.SerializerMethodField()
    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'date_close', 'score', 'status']
    def get_status(self, obj):
        return obj.get_status_display()


class ConcludedEnrollmentsListByDateSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')
    course = serializers.ReadOnlyField(source='course.name')    
    status = serializers.SerializerMethodField()
    class Meta:
        model = Enrollment
        fields = '__all__'
    def get_status(self, obj):
        return obj.get_status_display()

class StartedEnrollmentsListByDateSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')
    course = serializers.ReadOnlyField(source='course.name')    
    status = serializers.SerializerMethodField()
    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'date_enroll', 'score', 'status']
    def get_status(self, obj):
        return obj.get_status_display()

class StartedStudentListByDateSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')
    course = serializers.ReadOnlyField(source='course.name')    
    status = serializers.SerializerMethodField()
    class Meta:
        model = Enrollment
        fields = '__all__'
    def get_status(self, obj):
        return obj.get_status_display()

# class EnrollmentFullInfoSerializer(serializers.ModelSerializer):
#     student_name = serializers.ReadOnlyField(source='student.name')
#     course_name = serializers.ReadOnlyField(source='course.name')
#     course_description = serializers.ReadOnlyField(source='course.description')
#     course_duration = serializers.ReadOnlyField(source='course.duration')
#     enrollment_id = serializers.ReadOnlyField(source='enrollment.id')
#     enrollment_date = serializers.ReadOnlyField(source='enrollment.date_enroll')
#     enrollment_status = serializers.ReadOnlyField(source='enrollment.status')
#     class Meta:
#         model = EnrollmentFullInfo
#         fields = '__all__'