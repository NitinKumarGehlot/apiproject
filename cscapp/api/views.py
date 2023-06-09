from rest_framework.views import APIView
from cscapp.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

class CountriesList(APIView):

    def get(self, request, format=None):
        try:
            countries = Countries.objects.all()
            serializer = CountrySerializer(countries, many=True)
            return Response(serializer.data)
        except Exception:
            response = {"msg" : "Something went wrong"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

class StatesList(APIView):

    def get(self, request, country_id, format=None):
        if Countries.objects.filter(pk=country_id):
            try:
                country_obj = Countries.objects.get(pk=country_id)
                states = States.objects.filter(country=country_obj)
                serializer = StateSerializer(states, many=True)
                return Response(serializer.data)
            except Exception:
                response = {"msg" : "Something went wrong"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = {"msg" : "Please pass correct params."}
            return Response(response, status=status.HTTP_404_NOT_FOUND)


class CitiesList(APIView):

    def get(self, request, state_id, format=None):
        if States.objects.get(pk=state_id):
            try:
                state_obj = States.objects.get(pk=state_id)
                cities = Cities.objects.filter(state=state_obj)
                serializer = CitySerializer(cities, many=True)
                return Response(serializer.data)
            except Exception:
                response = {"msg" : "Something went wrong"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST) 
        else:
            response = {"msg" : "Please pass correct params."}
            return Response(response, status=status.HTTP_404_NOT_FOUND)


class CountryCitiesList(APIView):

    def get(self, request, country_id, format=None):
        if Countries.objects.get(pk=country_id):
            try:
                country_obj = Countries.objects.get(pk=country_id)
                cities = Cities.objects.filter(country=country_obj)
                serializer = CitySerializer(cities, many=True)
                return Response(serializer.data)
            except Exception:
                response = {"msg" : "Something went wrong"}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {"msg" : "Please pass correct params."}
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        