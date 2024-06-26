# Generated by Django 5.0.6 on 2024-06-26 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=40)),
                ('course_name', models.CharField(max_length=100)),
                ('course_credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_usn', models.CharField(max_length=20)),
                ('student_name', models.CharField(max_length=100)),
                ('student_sem', models.IntegerField()),
                ('enrolment', models.ManyToManyField(to='myapp.course')),
            ],
        ),
    ]
