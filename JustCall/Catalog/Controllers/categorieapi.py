from django.core import serializers
from Catalog.models import Categories
from Catalog.serializers.CategorieSerializer import CategoriesSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class CreateCategorie(APIView):
    def get(self, request,*args,**kwargs):
        categorie = Categories.objects.all()
        serializer = CategoriesSerializer(categorie, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategoriesSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
