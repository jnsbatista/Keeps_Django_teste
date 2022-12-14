# Generated by Django 4.1.2 on 2022-10-29 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0026_alter_enrollment_justification'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrollmentFullInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_description', models.CharField(max_length=300)),
                ('course_duration', models.DecimalField(decimal_places=1, max_digits=5)),
                ('enrollment_id', models.PositiveIntegerField()),
                ('enrollment_date', models.DateField(auto_now=True)),
                ('enrollment_status', models.CharField(max_length=1)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.course')),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearning.student')),
            ],
        ),
    ]
