from rest_framework import serializers
from .models import Course, Week

class WeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Week
        fields = ['id','course','week', 'date_01', 'date_02', 'module']

class CourseSerializer(serializers.ModelSerializer):
    weeks = WeekSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'course_name', 'course_description', 'start_date', 'trial_date', 'class_duration', 'course_duration', 'total_class_duration', 'weekend_classes', 'student_support_session', 'support_session_duration', 'weeks']
