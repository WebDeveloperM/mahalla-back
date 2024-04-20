from rest_framework import serializers
from task.models import *
from task.serialazers.region import RegionSerializer

from task.models import House, Person


class DistrictSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    houses = serializers.PrimaryKeyRelatedField(many=True, queryset=House.objects.all())
    persons = serializers.PrimaryKeyRelatedField(many=True, queryset=Person.objects.all())

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['region'] = RegionSerializer(instance.region).data
        return data


class DistrictSimpleSerializer(serializers.Serializer):
    name = serializers.CharField()
