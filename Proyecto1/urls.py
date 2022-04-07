"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import saludo, despedida, dame_fecha, calcula_edad, calcula_edad2, documento_externo
from .views import documento_externo2, uso_clases, uso_loader, uso_shortcuts, curso_c, curso_CSS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('chaoerror/', despedida),
    path('fecha/', dame_fecha),
    path('edades/<int:agno>', calcula_edad),
    path('edades2/<int:edad>/<int:agno>', calcula_edad2),
    path('documentos/', documento_externo),
    path('documentos2/', documento_externo2),
    path('clases/', uso_clases),
    path('loader/', uso_loader),
    path('short/', uso_shortcuts),
    path('cursoc/', curso_c),
    path('cursocss/', curso_CSS),
]
