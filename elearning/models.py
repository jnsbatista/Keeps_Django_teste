from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    holder_image = models.ImageField(upload_to=None, null=True, height_field=None, width_field=None, max_length=100)
    duration = models.DecimalField(max_digits=5, decimal_places=1)
    date_created = models.DateField(auto_now=True, auto_now_add=False)
    date_updated = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to=None, null=True, height_field=None, width_field=None, max_length=100)
    date_created = models.DateField(auto_now=True, auto_now_add=False)
    date_updated = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    STATUS = (
        ('C', 'Cursando'),
        ('A', 'Aprovado'),
        ('D', 'Desistente'),
        ('R', 'Reprovado')        
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enroll = models.DateField(auto_now=True, auto_now_add=False)
    date_close = models.DateField(null=True)
    score = models.PositiveIntegerField(null=True, default=1)
    status = models.CharField(max_length=1, choices=STATUS, null=False, default='C')
    justification = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.student

# class EnrollmentFullInfo(models.Model):
#     student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
#     course_description = models.CharField(max_length=300)
#     course_duration = models.DecimalField(max_digits=5, decimal_places=1)
#     enrollment_id = models.PositiveIntegerField()
#     enrollment_date = models.DateField(auto_now=True, auto_now_add=False)
#     enrollment_status = models.CharField(max_length=1, null=False)

#     def __str__(self):
#         return self.student_name