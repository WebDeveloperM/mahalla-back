from rest_framework import serializers

from task.serialazers.street import StreetSimpleSerializer


class HouseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    ownership = serializers.CharField()
    number_of_appartment = serializers.IntegerField()
    date_of_birth = serializers.DateField(read_only=True)
    category_appartment = serializers.CharField()
    street = serializers.CharField()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['street'] = StreetSimpleSerializer(instance.street).data
        return data


class HouseSimpleSerializer(serializers.Serializer):
    ownership = serializers.CharField()
    number_of_appartment = serializers.IntegerField()
    street = serializers.CharField()
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['street'] = StreetSimpleSerializer(instance.street).data
        return data