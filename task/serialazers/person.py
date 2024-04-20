from rest_framework import serializers
from task.models import Person
from task.serialazers.house import HouseSimpleSerializer


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    house_id = serializers.IntegerField()
    residential_status = serializers.CharField()
    passport_number = serializers.CharField(max_length=255)
    date_of_birth = serializers.DateField()
    jshshir = serializers.CharField()
    phone_number = serializers.CharField(max_length=255)
    appartment_type = serializers.CharField(max_length=255)
    cadastr_number = serializers.CharField(max_length=255)
    status_of_registration = serializers.CharField(max_length=255)
    time_registered = serializers.DateField()
    address_of_passport = serializers.CharField(max_length=255)
    image = serializers.FileField()
    district_id = serializers.IntegerField()
    region_id = serializers.IntegerField()
    neighborhood_id = serializers.IntegerField()
    street_id = serializers.IntegerField()
    age = serializers.IntegerField()
    gender = serializers.CharField()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['house_id'] = HouseSimpleSerializer(instance.house).data
        return data

    def create(self, validated_data):
        return Person.objects.create(**validated_data)


class PersonSimpleSerializer(serializers.Serializer):
    name = serializers.CharField()
