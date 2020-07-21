from django.db import models

class Country(models.Model):
	code = models.CharField(max_length=2)
	name = models.CharField(max_length=52)
	population = models.IntegerField()

	def __str__(self):
		return self.name