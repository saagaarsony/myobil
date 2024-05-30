from rest_framework import serializers
from .models import Bus_Details, Per_Details

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Per_Details
        fields = '__all__'

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus_Details
        fields = '__all__'
