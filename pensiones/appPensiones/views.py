from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Trabajador

# Create your views here.
def index(request):
    return render(request, "appPensiones/index.html", {})

def agrega_trabajador_forma(request):
    nombre = request.POST.get("nombre")
    edadActual = int(request.POST.get("edadActual"))
    edadRetiro = int(request.POST.get("edadRetiro"))
    saldoAcumulado = float(request.POST.get("saldoAcumulado"))
    ahorroMensual = float(request.POST.get("ahorroMensual"))
    genero = request.POST.get("genero")
    trabajador = Trabajador(  nombre=nombre, 
                                edadActual=edadActual, 
                                edadRetiro=edadRetiro, 
                                saldoAcumulado=saldoAcumulado,
                                ahorroMensual = ahorroMensual,
                                genero = genero)
    trabajador.save()
    return render(request, 'appPensiones/agrega_trabajador_forma.html', {'trabajador': trabajador})

def listado_trabajadores(request):
    trabajadores = Trabajador.objects.order_by('nombre')
    #template = loader.get_template('myfirstapp/index.html')
    context = {
        'trabajadores': trabajadores,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, "appPensiones/listado_trabajadores.html", context)