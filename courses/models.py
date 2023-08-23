from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()
    start_date = models.CharField(max_length=20)
    trial_date = models.CharField(max_length=20)
    class_duration = models.CharField(max_length=20)
    course_duration = models.CharField(max_length=20)
    total_class_duration = models.CharField(max_length=20)
    weekend_classes = models.CharField(max_length=100)
    student_support_session = models.CharField(max_length=100)
    support_session_duration = models.CharField(max_length=20)

    def __str__(self):
        return self.course_name


class Week(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    week = models.CharField(max_length=20)
    date_01 = models.CharField(max_length=20)
    date_02 = models.CharField(max_length=20)
    module = models.CharField(max_length=100)

    def __str__(self):
        return self.week

