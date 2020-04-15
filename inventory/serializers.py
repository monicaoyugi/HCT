from rest_framework import serializers
from inventory.models import ItemDonated, Hospital, Donor


class ItemDonatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDonated
        fields = '__all__'


class HospitalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class DonorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = '__all__'
