"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from libreria.views import home, saludo, create_product, list_prod, search_prod, create_binding, create_notebook, list_bind, list_notebook, quienes_somos , contacto

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path('home/', saludo, name="saludo"),
    path('productos/create-prod/', create_product, name="createprod"),
    path('productos/list-prod/', list_prod, name="list-prod"),
    path('productos/search-prod/', search_prod, name="search-prod"),
    path('productos/create-binding/', create_binding, name = 'createbinding'),
    path('productos/create-notebook/', create_notebook, name = 'create_notebook'),
    path('productos/list-bind/', list_bind, name = 'list-bind'),
    path('productos/list-notebook/', list_notebook, name = 'list-notebook'),
    path('quienes_somos/', quienes_somos, name = 'quienes_somos'),
    path('contacto/', contacto, name = 'contacto')

]
