# Generated by Django 3.2.5 on 2021-09-13 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_s_attendance_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='s_attendance',
            name='user_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]