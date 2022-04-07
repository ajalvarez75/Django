from cgitb import html
from datetime import datetime
from re import template
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.template.loader import get_template
from django.shortcuts import render

def saludo(request): # primera vista

    return HttpResponse("bienvenido a mi primera pagina con django")

def despedida(request): #segunda vista

    return HttpResponse('chao gran hp error')

def dame_fecha(request): #tercera vista

    fecha_actual=datetime.now()

    documento="""
    <html>
    <body>
    <h1> Fecha y hora actuales {} </h1>
    </body>
    </html>
    """ .format(fecha_actual)

    return HttpResponse(documento)

def calcula_edad(request, agno):

    edadActual=18
    periodo=agno-2022
    edadFutura=edadActual+periodo
    documento="""<html>
    <body>
    <h1> En el año {} tendras {} años </h1>
    </body>
    </html>
    """ .format(agno, edadFutura)

    return HttpResponse(documento)

def calcula_edad2(request, edad, agno):

    periodo=agno-2022
    edadFutura=edad+periodo
    documento="""<html>
    <body>
    <h1> En el año {} tendras {} años </h1>
    </body>
    </html>
    """ .format(agno, edadFutura)

    return HttpResponse(documento)
    
def documento_externo(request):

    doc_externo=open("C:/Users/Alvaro Javier/Desktop/Python/DJANGO/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context()

    documento=plt.render(ctx)

    return HttpResponse(documento)

def documento_externo2(request):

    nombre="Juan"

    apellido="Alvarez"

    ahora=datetime.now()

    doc_externo=open("C:/Users/Alvaro Javier/Desktop/Python/DJANGO/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre_persona":nombre, "apellido_persona":apellido, "momento_actual":ahora})
    #en lugar de relacion la variable nombre se puede colocar directamente el valor

    documento=plt.render(ctx)

    return HttpResponse(documento)


class Persona(object):

    def __init__(self, nombre, apellido) -> None:

        self.nombre=nombre
        self.apellido=apellido

def uso_clases(request):

    p1=Persona("Alvaro", "Alvarez")

    temas_del_curso=["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]

    ahora=datetime.now()

    doc_externo=open("C:/Users/Alvaro Javier/Desktop/Python/DJANGO/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temas_del_curso})

    documento=plt.render(ctx)

    return HttpResponse(documento)

def uso_loader(request):

    p1=Persona("Alvaro", "Alvarez")

    temas_del_curso=["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]

    ahora=datetime.now()

    doc_externo=loader.get_template('miplantilla.html')
    #tambien se puede ignorar/borrar el loader. por que previamente importamos get_template

    documento=doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temas_del_curso})

    return HttpResponse(documento)

def uso_shortcuts(request):

    p1=Persona("Alvaro", "Alvarez")

    temas_del_curso=["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]

    ahora=datetime.now()

    return render(request, "miplantilla.html", {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temas_del_curso})

def curso_c(request):

    fecha_actual=datetime.now()

    return render(request, "CursoC.html", {"dame_fecha": fecha_actual})

def curso_CSS(request):

    fecha_actual=datetime.now()

    return render(request, "cursoCSS.html", {"dame_fecha": fecha_actual})      