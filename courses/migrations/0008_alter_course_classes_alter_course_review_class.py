# Generated by Django 4.2.4 on 2023-09-07 17:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0007_remove_course_cyber_classes_course_classes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="classes",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="course",
            name="review_class",
            field=models.CharField(max_length=100),
        ),
    ]
