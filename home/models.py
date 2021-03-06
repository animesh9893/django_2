from django.db import models

# Create your models here.
class User(models.Model):
	user_name=models.CharField(max_length=20)
	password=models.CharField(max_length=200)

	def __str__(self):
		return self.user_name
	def check_password(self,p):
		return p==self.password

class SocialAccounts(models.Model):
	user_name=models.ForeignKey(User,on_delete=models.CASCADE)
	website_name = models.CharField(max_length=50)
	profile_url = models.URLField(max_length=200)

	def __str__(self):
		return self.website_name

class Carousel(models.Model):
	name = models.CharField(max_length=200)
	creation_time = models.DateTimeField(auto_now_add=True)
	valid_day = models.IntegerField() 
	photo = models.ImageField()
	display = models.BooleanField(default=True)
	def __str__(self):
		return self.name
	def get_img(self):
		return str(self.photo)
	@property
	def photo_url(self):
		if self.photo and hasattr(self.photo,'url'):
			return self.photo.url