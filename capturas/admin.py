from django.contrib import admin
from .models import ListaPrecios, PuntoVenta, PagoFolios, FormasPago, Asistentes

admin.site.register(ListaPrecios)
admin.site.register(PagoFolios)
admin.site.register(PuntoVenta)
admin.site.register(FormasPago)
admin.site.register(Asistentes)