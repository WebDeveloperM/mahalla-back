from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from task.models import House

from task.serialazers.house import HouseSerializer


class HouseView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        id = kwargs.get('id')
        if not id:
            return Response({"error": "Id not found"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            houses = House.objects.filter(street_id=id)
        except:
            return Response({"error": "Failed to retrieve district"}, status=status.HTTP_404_NOT_FOUND)
        serializer = HouseSerializer(houses, many=True)
        return Response(serializer.data)
