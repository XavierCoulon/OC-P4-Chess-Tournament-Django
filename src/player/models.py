from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Gender(models.Model):
	label = models.CharField(unique=True, max_length=128)


class Player(models.Model):
	first_name = models.CharField(unique=True, max_length=128, blank=False)
	last_name = models.CharField(unique=True, max_length=128, blank=False)
	ranking = models.PositiveIntegerField(unique=True, validators=[MinValueValidator(1)])
	birth_date = models.DateField(blank=False)
	gender = models.ForeignKey(to=Gender, on_delete=models.PROTECT)
	description = models.CharField(unique=True, max_length=128, blank=False)

	def get_absolute_url(self):
		return reverse("players:menu")

	def __str__(self):
		return self.first_name
