from datetime import datetime

from django.db.models import Q
from rest_framework import serializers
from task.models import District, Neighborhood, Street, House, Person
from task.models import Region


# class RegionSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     districts = serializers.PrimaryKeyRelatedField(many=True, queryset=District.objects.all())
#     neighborhoods = serializers.PrimaryKeyRelatedField(many=True, queryset=Neighborhood.objects.all())
#     streets = serializers.PrimaryKeyRelatedField(many=True, queryset=Street.objects.all())
#     houses = serializers.PrimaryKeyRelatedField(many=True, queryset=House.objects.all())
#     persons = serializers.PrimaryKeyRelatedField(many=True, queryset=Person.objects.all())


class RegionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    districts = serializers.PrimaryKeyRelatedField(many=True, queryset=District.objects.all())
    neighborhoods = serializers.PrimaryKeyRelatedField(many=True, queryset=Neighborhood.objects.all())
    streets = serializers.PrimaryKeyRelatedField(many=True, queryset=Street.objects.all())
    houses = serializers.PrimaryKeyRelatedField(many=True, queryset=House.objects.all())
    persons = serializers.PrimaryKeyRelatedField(many=True, queryset=Person.objects.all())

    class Meta:
        model = Region
        fields = '__all__'