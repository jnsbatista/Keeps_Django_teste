# Generated by Django 4.1.2 on 2022-10-14 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0019_alter_enrollment_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='score',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
