# Generated by Django 5.0.6 on 2024-06-26 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_course_course_credits'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=200)),
                ('ptopic', models.CharField(max_length=200)),
                ('plangauges', models.CharField(max_length=200)),
                ('pduration', models.IntegerField()),
            ],
        ),
    ]