# Generated by Django 2.1.7 on 2019-05-21 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='image',
        ),
    ]