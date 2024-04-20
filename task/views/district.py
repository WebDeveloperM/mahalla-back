from django.db.models import Count, Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from task.models import District


class DistrictView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        id = kwargs.get('id')
        if not id:
            return Response({"error": "Id not found"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            districts = District.objects.filter(region_id=id)

            districts = (districts.prefetch_related('neighborhoods', 'neighborhoods__streets')
            .annotate(
                count_neighborhoods=Count('neighborhoods', distinct=True),
                count_neighbourhoods=Count('neighborhoods__streets', distinct=True),
                count_young_people=Count('persons', distinct=True,
                                         filter=Q(persons__age__gte=18) & Q(persons__age__lte=30)),
                count_people=Count('persons', distinct=True),
                count_houses=Count('houses', distinct=True),
                count_residention=Count('persons', distinct=True, filter=Q(persons__residential_status='shaxsiy')),
                count_femail=Count('persons', distinct=True, filter=Q(persons__gender='Ayol')),
                count_pensioner=Count('persons', distinct=True, filter=Q(persons__age__gte='60'))

            ))
            # district = District.objects.raw('SELECT * FROM task_district WHERE id = %s', [id,])
        except:
            return Response({"error": "Failed to retrieve district"}, status=status.HTTP_404_NOT_FOUND)
        # serializer = DistrictSerializer(districts, many=True)
        return Response(districts.values(), status=status.HTTP_200_OK)
