import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from task.models import House
from task.models import Person
from task.serialazers.person import PersonSerializer


class PersonView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        id = kwargs.get('id')
        if not id:
            return Response({"error": "Id not found"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            house = House.objects.get(id=id)
            print(house.region)
            persons = Person.objects.filter(house_id=id)
        except:
            return Response({"error": "Failed to retrieve district"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)


class AddPersonView(APIView):

    def post(self, request, *args, **kwargs):
        print(request.data, "-------------------------------------------------")
        person = Person.objects.filter(passport_number=request.data.get('passport_number'))
        house = House.objects.get(id=request.data.get('house_id'))
        print(house, "11111111111111111111111111")
        if person:
            return Response({"error": "Bunday foydalanuvchi mavjud!!!"}, status=status.HTTP_400_BAD_REQUEST)
        request.data['district_id'] = house.district_id
        request.data['region_id'] = house.region_id
        request.data['district_id'] = house.district_id
        request.data['neighborhood_id'] = house.neighborhood_id
        request.data['house_id'] = house.id
        request.data['street_id'] = house.street_id
        age = datetime.date.today().year - int(request.data.get('date_of_birth')[:4])
        request.data['age'] = age
        print(request.data, "0000000000000000000000000")
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetPersonView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if not id:
            return Response({"error": "Id not found"}, status=status.HTTP_400_BAD_REQUEST)

        try:

            persons = Person.objects.filter(id=id)
        except:
            return Response({"error": "Failed to retrieve district"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
