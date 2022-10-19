from django.contrib import admin
from elearning.models import *

class Courses(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'holder_image', 'duration', 'date_created', 'date_updated')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Course, Courses)

class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'nickname', 'phone', 'avatar', 'date_created', 'date_updated')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(Student, Students)

class Enrollments(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'date_enroll', 'date_close', 'score', 'status')
    list_display_links = ('id', 'student', 'course')
    search_fields = ('student',)

admin.site.register(Enrollment, Enrollments)