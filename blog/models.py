from django.db import models

class Post(models.Model):
	created = models.DateTimeField(auto_now_add=True, db_index=True)
	title = models.CharField(blank=True,max_length=255)
	img = models.ImageField(blank=True,upload_to='media/')
	content = models.TextField()

	def __unicode__(self):
		return self.title