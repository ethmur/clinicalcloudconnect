from django.db import models
		
class HealthProvider(models.Model):
	
	name = models.TextField(max_length=100)
	address = models.TextField(max_length=100, default="")
	tele = models.TextField(max_length=100, default="")
	def __str__(self):
		return "HealthProvider(name={})".format(self.name)
		
class User(models.Model):
	
	name = models.TextField(max_length=100)
	dob = models.TextField(max_length=100, default="")
	address = models.TextField(max_length=100, default="")
	tele = models.TextField(max_length=100, default="")
	health_provider = models.TextField(max_length=100, default="")
	employer = models.TextField(max_length=100, default="")
	sex = models.TextField(max_length=100, default="")
	medical_conditions = models.TextField(max_length=100, default="")
	current_medications = models.TextField(max_length=100, default="")
	
	def __str__(self):
		return "Person(name={})".format(self.name)
		
class ProvidesFor(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	hp = models.ForeignKey(HealthProvider, on_delete=models.CASCADE)
		
		
class FilePost(models.Model):
	file = models.FileField(upload_to = '.')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return ("Name: " + str(self.file.name) + ", User: " + str(self.user))
