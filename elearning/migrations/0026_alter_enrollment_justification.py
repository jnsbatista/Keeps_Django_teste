# Generated by Django 4.1.2 on 2022-10-18 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0025_enrollment_justification_alter_enrollment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='justification',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
