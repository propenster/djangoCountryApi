from rest_framework import serializers
from . models import Country

class CountrySerializer(serializers.ModelSerializer):
	"""docstring for ClassName"""
	class Meta:
		model = Country
		fields = ['code', 'name', 'population']
			
		