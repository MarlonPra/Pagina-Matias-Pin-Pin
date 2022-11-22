from django.urls import path, include
from . import views

app_name = 'main'


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('carta', views.carta, name='carta'),
    path('carta/Heladeria', views.heladeria, name='heladeria'),
    path('carta/Comida Rapida', views.comrapida, name='comida_rapida'),
    path('carta/Pizzeria', views.pizzeria, name='pizzeria'),
    path('carta/Bebidas', views.bebidas, name='bebidas'),
    path('galeria', views.galeria, name='galeria'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_request, name='logout'),
    path('perfil', views.perfil, name='perfil'),
    path('pedidos', views.pedidos, name='pedidos'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name='agregar'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar'),
    path('restar/<int:producto_id>/', views.restar_producto, name='restar'),
    path('limpiar/', views.limpiar_carro, name='limpiar'),
    path('procesar/', views.procesar_pedido, name='procesar'),
    path('completar/<int:pedido_id>/', views.eliminar_pedido, name='completar'),
]

