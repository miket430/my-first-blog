from django.db import models
from django.utils import timezone
# Create your models here.

''' 
models.Model tells Django it should be saved 
in the database.
CharField: Limited number of characters
TextField: Unlimited
python manage.py makemigrations $(App_Name) to inform Django
that changes in the model
python manage.py migrate blog to finalize migration
Register model in App_Name/admin.py
'''
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	create_date = models.DateTimeField(
		default = timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title