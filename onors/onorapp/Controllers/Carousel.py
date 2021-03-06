from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.core import serializers
from onorapp.Serializers.CarouselSerializer import CarouselSerializers
from django.http import JsonResponse
from onorapp.models import Carousel
from django.http import Http404
from rest_framework import status

class getUpdateDeleteCarousel(APIView):
    def get_object(self,id):
        try:
            return Carousel.objects.get(id=id)
        except:
            raise Http404

    def get(self, request, id, format=None):
        try:
            get=self.get_object(id)
            serializer=CarouselSerializers(get)
            return Response(serializer.data)
        except Http404:
            return JsonResponse({"message:":"listings not found"})

    def put(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            serializer=CarouselSerializers(obj,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return JsonResponse({"message":"data not updated"})

    def delete(self,request,id,format=None):
        try:
            obj=self.get_object(id)
            obj.delete()
            return Response({"message":"data  deleted"})
        except Http404:
            return JsonResponse({"message":"data not deleted"})
