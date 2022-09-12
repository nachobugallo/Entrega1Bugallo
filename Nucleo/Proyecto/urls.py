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
from django.conf import Settings
from django.conf.urls.static import static
from libreria.views import home, saludo, update_product, create_product, delete_product, list_prod, search_prod, create_binding, create_notebook, list_bind, list_notebook, quienes_somos , contacto
from users.views import login_request, register, my_profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path('index/', saludo, name="saludo"),
    path('contacto/', contacto, name = 'contacto'),
    path('users/login/', login_request, name = 'login'),
    path('users/register/', register, name='register'),
    path('users/logout/', LogoutView.as_view(template_name  = 'users/logout.html'), name = 'logout'),
    path('users/my_profile', my_profile, name = 'my_profile'),
    path('about/', quienes_somos, name = 'quienes_somos'),
    path('productos/create-prod/', create_product, name="createprod"),
    path('productos/delete_product/<int:pk>/', delete_product, name="delete_product"),
    path('productos/update_product/<int:pk>/', update_product, name="update_product"),
    path('productos/lista-prod/', list_prod, name="lista-prod"),
    path('productos/search-prod/', search_prod, name="search-prod"),
    path('productos/create-binding/', create_binding, name = 'createbinding'),
    path('productos/create-notebook/', create_notebook, name = 'create_notebook'),
    path('productos/list-bind/', list_bind, name = 'list-bind'),
    path('productos/list-notebook/', list_notebook, name = 'list-notebook'),
] #+ static(Settings.MEDIA_URL, document_root=Settings.MEDIA_ROOT)
