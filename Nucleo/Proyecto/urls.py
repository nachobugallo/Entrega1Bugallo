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

from django.contrib import admin
from django.urls import path
from libreria.views import saludo, list_prod, create_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', saludo, name="saludo"),
    path('productos/', list_prod, name="listprod"),
    path('nuevo/', create_product, name="createprod"),
    path('libreria/', "libreria", libreria='libreria'),
    path('quienes_somos/', "quienes_somos", name="quienes_somos"),
    path('sucursarles/', "sucursarles", name="sucursarles"),
    path('contacto/', "contacto", name="contacto"),
]
