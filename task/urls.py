from django.urls import path
from task.views.district import DistrictView
from task.views.house import HouseView
from task.views.neighborhood import NeighborhoodView
from task.views.person import AddPersonView, GetPersonView, PersonView
from task.views.region import RegionView
from task.views.street import StreetView

urlpatterns = [
    path("region/", RegionView.as_view()),
    path("district/<int:id>/", DistrictView.as_view()),
    path("neighborhood/<int:id>/", NeighborhoodView.as_view()),
    path("street/<int:id>/", StreetView.as_view()),
    path("house/<int:id>/", HouseView.as_view()),
    path("add-person/", AddPersonView.as_view()),
    path("person/<int:id>/", PersonView.as_view()),
    path("getperson/<int:id>/", GetPersonView.as_view()),
]
