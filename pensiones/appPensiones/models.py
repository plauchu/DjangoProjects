from django.db import models

# Create your models here.
class Trabajador(models.Model):
    nombre = models.CharField(max_length=200)
    edadActual = models.IntegerField(default=0)
    edadRetiro = models.IntegerField(default=0)
    saldoAcumulado = models.FloatField(default=0.0)
    ahorroMensual = models.FloatField(default=0.0)
    genero = models.CharField(max_length=10)
    def __str__(self):
        resp = "Nombre: "+self.nombre
        resp += "\t|\tEdadActual: "+str(self.edadActual)
        resp += "\t|\tEdad de retiro: "+str(self.edadRetiro)
        resp += "\t|\tGénero: " +self.genero
        resp += "\t|\tSaldo acumulado: $"+str(self.saldoAcumulado)
        resp += "\t|\tAhorro mensual: $"+str(self.ahorroMensual)
        resp += "\t|\tPensión esperada: $"+str(self.getPension())
        return resp
    
    def getPension(self):
        return (float(self.edadRetiro-self.edadActual))*12*self.ahorroMensual