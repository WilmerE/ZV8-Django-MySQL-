from django.db import models

# Create your models here.
class Circulares_Despachadas(models.Model):
	no_circ = models.CharField('No. Circular', max_length=10)
	fecha = models.DateTimeField(auto_now_add=True, blank=True)
	dirigido = models.TextField('Dirigido', max_length=500)
	resumen = models.TextField('Resumen', max_length=500)
	fecha_recibido = models.DateTimeField(auto_now_add=True, blank=True)
	nota = models.TextField('Nota', max_length=500)

	def __str__(self):
		return str(self.no_circ)

	class Meta:
		db_table = 'circ_desp'
		verbose_name = 'Circular Despachado'
		verbose_name_plural = 'Circulares Despachados'

class Circulares_DGC(models.Model):
	no_circ = models.CharField('No. Circular', max_length=10)
	fecha = models.DateTimeField(auto_now_add=True, blank=True)
	dirigido = models.TextField('Dirigido', max_length=500)
	resumen = models.TextField('Resumen', max_length=500)
	fecha_recibido = models.DateTimeField(auto_now_add=True, blank=True)
	nota = models.TextField('Nota', max_length=500)

	def __str__(self):
		return str(self.no_circ)

	class Meta:
		db_table = 'circ_dgc'
		verbose_name = 'Circular DGC'
		verbose_name_plural = 'Circulares DGC'

class Circulares_Recibidos(models.Model):
	no_circ = models.CharField('No. Circular', max_length=10)
	fecha = models.DateTimeField(auto_now_add=True, blank=True)
	dirigido = models.TextField('Dirigido', max_length=500)
	resumen = models.TextField('Resumen', max_length=500)
	fecha_recibido = models.DateTimeField(auto_now_add=True, blank=True)
	nota = models.TextField('Nota', max_length=500)

	def __str__(self):
		return str(self.no_circ)

	class Meta:
		db_table = 'circ_rec'
		verbose_name = 'Circular Recibido'
		verbose_name_plural = 'Circulares Recibidos'

class Circulares_Recibidos_DGC(models.Model):
	no_circ = models.CharField('No. Circular', max_length=10)
	fecha = models.DateTimeField(auto_now_add=True, blank=True)
	dirigido = models.TextField('Dirigido', max_length=500)
	resumen = models.TextField('Resumen', max_length=500)
	fecha_recibido = models.DateTimeField(auto_now_add=True, blank=True)
	nota = models.TextField('Nota', max_length=500)

	def __str__(self):
		return str(self.no_circ)

	class Meta:
		db_table = 'circ_rec_dgc'
		verbose_name = 'Circular Recibido DGC'
		verbose_name_plural = 'Circulares Recibidos DGC'