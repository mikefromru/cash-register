from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
    
    # def create(self,validated_data):
    #     return Bill.objects.create(**validated_data)
        
