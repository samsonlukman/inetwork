# Generated by Django 4.1.7 on 2023-07-25 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_alter_student_phone_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
