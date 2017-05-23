from django.db import models

# Create your models here.

class Quote(models.Model):
	quote_text = models.CharField(max_length=1000)
	quote_owner = models.CharField(max_length=100)
	def __str__(self):
		return self.quote_text