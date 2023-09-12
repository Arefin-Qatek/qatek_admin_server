from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Course, Week
from .serializers import CourseSerializer, WeekSerializer


class CourseAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, course_id=None):
        if course_id is not None:
            try:
                course = Course.objects.get(id=course_id)
                serializer = CourseSerializer(course)
                return Response(serializer.data)
            except Course.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            courses = Course.objects.all()
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# to delete all the courses
    def delete(self, request):
        courses = Course.objects.all()
        courses.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    def put(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
class WeekAPIView(APIView):

    def get_weeks_by_course(self, course_id):
        try:
            weeks = Week.objects.filter(course_id=course_id)
            serializer = WeekSerializer(weeks, many=True)
            return serializer.data
        except Week.DoesNotExist:
            raise NotFound("Weeks not found for the given course ID.")

    def get(self, request, week_id=None, course_id=None):
        if week_id is not None:
            try:
                week = Week.objects.get(id=week_id)
                serialized_week = WeekSerializer(week).data
                return Response(serialized_week)
            except Week.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        elif course_id is not None:
            weeks = self.get_weeks_by_course(course_id)
            return Response(weeks)
        else:
            weeks = Week.objects.all()
            serialized_weeks = WeekSerializer(weeks, many=True).data
            return Response(serialized_weeks)

    def post(self, request):
        serializer = WeekSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, week_id):
        try:
            week = Week.objects.get(id=week_id)
        except Week.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = WeekSerializer(week, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, week_id):
        try:
            week = Week.objects.get(id=week_id)
        except Week.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        week.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#For Public View
class CourseListAPIView(APIView):

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class WeekListAPIView(APIView):

    def get_weeks_by_course(self, course_id):
        try:
            weeks = Week.objects.filter(course_id=course_id)
            serializer = WeekSerializer(weeks, many=True)
            return serializer.data
        except Week.DoesNotExist:
            raise NotFound("Weeks not found for the given course ID.")

    def get(self, request, week_id=None, course_id=None):
        if week_id is not None:
            try:
                week = Week.objects.get(id=week_id)
                serialized_week = WeekSerializer(week).data
                return Response(serialized_week)
            except Week.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        elif course_id is not None:
            weeks = self.get_weeks_by_course(course_id)
            return Response(weeks)
        else:
            weeks = Week.objects.all()
            serialized_weeks = WeekSerializer(weeks, many=True).data
            return Response(serialized_weeks)