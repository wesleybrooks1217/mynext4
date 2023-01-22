from rest_framework import serializers
from .models import Units

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Units
        fields = ("id", "name", "description")