from django.db import models


class Gender(models.Model):
	label = models.CharField(unique=True, max_length=128)


class Player(models.Model):
	first_name = models.CharField(unique=True, max_length=128, blank=False)
	last_name = models.CharField(unique=True, max_length=128, blank=False)
	ranking = models.IntegerField(unique=True, )
	birth_date = models.DateField(blank=False)
	gender = models.ForeignKey(to=Gender, on_delete=models.PROTECT)
	description = models.CharField(unique=True, max_length=128, blank=False)

	def __str__(self):
		""" Used to print a Player object """
		print(f"Player: {self.first_name} {self.last_name}  / ranking: {self.ranking}")
