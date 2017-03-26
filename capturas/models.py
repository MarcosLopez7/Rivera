from django.db import models

class PuntoVenta(models.Model):
    punto_venta = models.CharField(max_length=25)

    def __str__(self):
        return self.punto_venta


class ListaPrecios(models.Model):
    clave_precio = models.CharField(max_length=2)
    clave_descripcion = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    moneda = models.CharField(max_length=5)

    def __str__(self):
        return self.clave_precio


class Asistentes(models.Model):
    folio = models.IntegerField()
    fol_status = models.CharField(max_length=1)
    no_asistio = models.BooleanField(default=False)
    pais_procedencia = models.CharField(max_length=30, null=True)
    estado_procedencia = models.CharField(max_length=30, null=True)
    ciudad_procedencia = models.CharField(max_length=30, null=True)
    esposo_apellido_paterno = models.CharField(max_length=25)
    esposo_apellido_materno = models.CharField(max_length=25)
    esposo_nombres = models.CharField(max_length=25)
    esposo_edad = models.IntegerField(null=True)
    esposo_celular = models.CharField(max_length=25)
    esposo_otro_cel = models.CharField(max_length=25, null=True)
    esposo_correo = models.CharField(max_length=60, null=True)
    esposa_apellido_paterno = models.CharField(max_length=25)
    esposa_apellido_materno = models.CharField(max_length=25)
    esposa_nombres = models.CharField(max_length=25)
    esposa_edad = models.IntegerField(null=True)
    esposa_celular = models.CharField(max_length=25)
    esposa_otro_cel = models.CharField(max_length=25, null=True)
    esposa_correo = models.CharField(max_length=60, null=True)
    comentario = models.TextField(null=True)
    punto_venta = models.ForeignKey(PuntoVenta)
    clave_precio = models.ForeignKey(ListaPrecios)

    def __str__(self):
        return self.folio


class FormasPago(models.Model):
    forma_pago = models.CharField(max_length=15)
    forma_pago_describe = models.CharField(max_length=50)

    def __str__(self):
        return self.forma_pago


class PagoFolios(models.Model):
    pag_fecha = models.DateField()
    pago_referencia = models.CharField(max_length=20)
    pago_verificado = models.BooleanField(default=False)
    punto_venta = models.ForeignKey(PuntoVenta)
    precio = models.ForeignKey(ListaPrecios)
    folio = models.ForeignKey(Asistentes)
    forma_pago = models.ForeignKey(FormasPago)

    def __str__(self):
        return "pago {0} del folio {1}".format(self.id, self.folio.folio)


