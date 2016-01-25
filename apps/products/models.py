from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Items(models.Model):
	price = models.FloatField()
	productName = models.TextField(max_length=255)
	brand = models.TextField(max_length=255)
	description = models.TextField(max_length=255)
	created_at = models.DateField()
	class Meta:
		db_table='items'