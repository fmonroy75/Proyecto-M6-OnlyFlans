"""
URL configuration for OnlyFlans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.urls import path
from carrito import views


urlpatterns = [
    path("", views.carrito, name="carrito"),
    path("agregar/<int:flan_id>/", views.agregar_al_carrito, name="agregar_al_carrito"),
    path(
        "eliminar/<int:item_id>/",
        views.eliminar_del_carrito,
        name="eliminar_del_carrito",
    ),
]
