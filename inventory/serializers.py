from rest_framework import serializers
from inventory.models import Item, Hospital


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class HospitalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'
