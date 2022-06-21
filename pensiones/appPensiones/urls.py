#from django.contrib import admin
from django.urls import path

from . import views

app_name = 'appPensiones'

urlpatterns = [
    path('', views.index,name="index"),
    path('agrega_trabajador_forma', views.agrega_trabajador_forma,name="agrega_trabajador_forma"),
    path('listado_trabajadores', views.listado_trabajadores, name = "listado_trabajadores"),
]