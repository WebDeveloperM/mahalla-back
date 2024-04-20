from rest_framework import serializers


from task.serialazers.neighborhood import NeighborhoodSimpleSerializer

from task.models import Person, House


class StreetSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    persons = serializers.PrimaryKeyRelatedField(many=True, queryset=Person.objects.all())
    houses = serializers.PrimaryKeyRelatedField(many=True, queryset=House.objects.all())

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['neighborhood'] = NeighborhoodSimpleSerializer(instance.neighborhood).data
        return data

class StreetSimpleSerializer(serializers.Serializer):
    name = serializers.CharField()
