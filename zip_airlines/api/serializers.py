import math

from django.conf import settings
from rest_framework import serializers

from api.models import Airplane


class AirplaneMultipleSerializer(serializers.ListSerializer):

    def create(self, validated_data):
        planes = [Airplane(**item) for item in validated_data]
        return Airplane.objects.bulk_create(planes)


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = '__all__'
        list_serializer_class = AirplaneMultipleSerializer


class AirplaneSpecSerializer(AirplaneSerializer):
    flight_duration = serializers.SerializerMethodField()
    total_fuel_consumption = serializers.SerializerMethodField()
    fuel_capacity = serializers.SerializerMethodField()

    class Meta:
        model = Airplane
        fields = ['id', 'name', 'flight_duration', 'total_fuel_consumption', 'fuel_capacity']

    def get_total_fuel_consumption(self, obj: Airplane):
        """Calculates fuel consumption rate based on the given data"""
        fuel_consumption = math.log(obj.id, 2) * settings.FUEL_CONSUMPTION_MULTIPLIER
        total_calculated_fc = fuel_consumption + obj.passengers * settings.FUEL_CONS_PER_PASSENGER
        return obj.base_fuel_consumption + total_calculated_fc

    def get_fuel_capacity(self, obj: Airplane):
        return obj.base_fuel_capacity + obj.id * settings.FUEL_CAPACITY_BASE_MULTIPLIER

    def get_flight_duration(self, obj: Airplane):
        return self.get_fuel_capacity(obj) // self.get_total_fuel_consumption(obj)
