# Generated by Django 3.2.5 on 2021-09-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks_app', '0012_alter_student_main_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_main',
            name='exam',
            field=models.CharField(max_length=20000, null=True),
        ),
    ]
