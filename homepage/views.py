from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import HomePageContent
from .serializers import HomePageContentSerializer
from rest_framework.permissions import IsAuthenticated

class HomePageContentListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None, format=None):  # Updated to use 'id'
        if id is None:
            queryset = HomePageContent.objects.all()
            serializer = HomePageContentSerializer(queryset, many=True)
        else:
            instance = get_object_or_404(HomePageContent, id=id)
            serializer = HomePageContentSerializer(instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = HomePageContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        instance = get_object_or_404(HomePageContent, id=id)

        serializer = HomePageContentSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        instance = get_object_or_404(HomePageContent, id=id)

        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#For Public View
class HomePageContentPublicView(APIView):
    def get(self, request, id=None, format=None):  # Updated to use 'id'
        if id is None:
            queryset = HomePageContent.objects.all()
            serializer = HomePageContentSerializer(queryset, many=True)
        else:
            instance = get_object_or_404(HomePageContent, id=id)
            serializer = HomePageContentSerializer(instance)

        return Response(serializer.data, status=status.HTTP_200_OK)