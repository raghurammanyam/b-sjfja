from rest_framework import serializers
from Catalog.models import MainPage

class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPage
        fields = '__all__'
