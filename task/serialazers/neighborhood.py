from rest_framework import serializers
from task.models import Person, House
from task.serialazers.district import DistrictSimpleSerializer


class NeighborhoodSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    persons = serializers.PrimaryKeyRelatedField(many=True, queryset=Person.objects.all())
    houses = serializers.PrimaryKeyRelatedField(many=True, queryset=House.objects.all())

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['district'] = DistrictSimpleSerializer(instance.district).data
        return data


class NeighborhoodSimpleSerializer(serializers.Serializer):
    name = serializers.CharField()
