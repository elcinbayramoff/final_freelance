from rest_framework import serializers
from .models import Position

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name','name_en','name_az','salary', 'department', 'created_at', 'updated_at']
