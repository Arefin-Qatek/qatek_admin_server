# Generated by Django 4.2.3 on 2023-07-10 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('course_description', models.TextField()),
                ('start_date', models.DateField()),
                ('trial_date', models.DateField()),
                ('class_duration', models.CharField(max_length=20)),
                ('course_duration', models.CharField(max_length=20)),
                ('total_class_duration', models.CharField(max_length=20)),
                ('weekend_classes', models.CharField(max_length=100)),
                ('student_support_session', models.CharField(max_length=100)),
                ('support_session_duration', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.CharField(max_length=20)),
                ('date_01', models.DateField()),
                ('date_02', models.DateField()),
                ('module', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
    ]
