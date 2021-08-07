from django.db import models
from django.utils import timezone

# Create your models here.
class Member(models.Model):
	firstname = models.CharField(max_length = 200)
	lastname = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	birthdate = models.CharField(max_length = 200)
	phone = models.CharField(max_length = 200)
	registertime = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return str(self.firstname)

 