# Generated by Django 5.0.6 on 2024-06-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_credits',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]