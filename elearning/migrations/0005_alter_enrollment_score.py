# Generated by Django 4.1.2 on 2022-10-11 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0004_alter_course_holder_image_alter_enrollment_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='score',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True),
        ),
    ]
