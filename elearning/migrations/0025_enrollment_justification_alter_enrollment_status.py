# Generated by Django 4.1.2 on 2022-10-14 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0024_alter_enrollment_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='justification',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='status',
            field=models.CharField(choices=[('C', 'Cursando'), ('A', 'Aprovado'), ('D', 'Desistente'), ('R', 'Reprovado')], default='C', max_length=1),
        ),
    ]