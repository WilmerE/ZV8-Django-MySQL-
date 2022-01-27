from django.contrib import admin
from .models import *

# Register your models here.
class Circulares_DespachadasAdmin(admin.ModelAdmin):
	search_fields = ['no_circ']
	list_filter = ['dirigido','fecha', 'fecha_recibido']
	list_display = ['no_circ', 'fecha', 'dirigido', 'resumen', 'fecha_recibido', 'nota']
	date_hierarchy="fecha"

class Circulares_DGCAdmin(admin.ModelAdmin):
	search_fields = ['no_circ']
	list_filter = ['dirigido','fecha', 'fecha_recibido']
	list_display = ['no_circ', 'fecha', 'dirigido', 'resumen', 'fecha_recibido', 'nota']
	date_hierarchy="fecha"

class Circulares_RecibidosAdmin(admin.ModelAdmin):
	search_fields = ['no_circ']
	list_filter = ['dirigido','fecha', 'fecha_recibido']
	list_display = ['no_circ', 'fecha', 'dirigido', 'resumen', 'fecha_recibido', 'nota']
	date_hierarchy="fecha"

class Circulares_Recibidos_DGCAdmin(admin.ModelAdmin):
	search_fields = ['no_circ']
	list_filter = ['dirigido','fecha', 'fecha_recibido']
	list_display = ['no_circ', 'fecha', 'dirigido', 'resumen', 'fecha_recibido', 'nota']
	date_hierarchy="fecha"

admin.site.register(Circulares_Despachadas, Circulares_DespachadasAdmin)
admin.site.register(Circulares_DGC, Circulares_DGCAdmin)
admin.site.register(Circulares_Recibidos, Circulares_RecibidosAdmin)
admin.site.register(Circulares_Recibidos_DGC, Circulares_Recibidos_DGCAdmin)