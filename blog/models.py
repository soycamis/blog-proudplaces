from django.db import models

class Post(models.Model):
	creado = models.DateTimeField(auto_now_add=True, db_index=True)
	titulo = models.CharField(blank=True,max_length=255)
	img = models.ImageField(upload_to='media/')
	contenido = models.TextField()

	def __unicode__(self):
		return self.titulo