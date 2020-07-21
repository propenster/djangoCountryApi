from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Country
from . serializers import CountrySerializer

class CountryList(APIView):
	def get(self, request):
		country = Country.objects.all()
		serializer = CountrySerializer(country, many=True)
		return Response(serializer.data)

	def post():
		pass

		

