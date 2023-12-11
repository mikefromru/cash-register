from rest_framework import serializers
from .models import Item, Bill

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
 
class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'
 
    # def create(self,validated_data):
    #     return Bill.objects.create(**validated_data)
        
