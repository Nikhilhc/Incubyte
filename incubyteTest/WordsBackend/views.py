from django.shortcuts import render
from django.http import Http404
from .serializers import WordSerializer
from .models import Words

from rest_framework.views import APIView
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.

class WordsListView(APIView):

    def get(self,request):
        queryset = Words.objects.all()
        serializer = WordSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        word = Words.objects.get(pk=pk)
        serializer = WordSerializer(word,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WordsDetailView(APIView):

    def get_object(self,pk):
        try:
            return Words.objects.get(pk=pk)
        except Words.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        queryset = self.get_object(pk)
        serializer = WordSerializer(queryset)
        return Response(serializer.data)

    def patch(self,request,pk):
        word = self.get_object(pk)
        serializer = WordSerializer(word,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        word = self.get_object(pk)
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
