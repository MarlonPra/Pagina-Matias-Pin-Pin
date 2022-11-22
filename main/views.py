from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as login_auth
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .carro import Carro
from .context_processor import importe_total_carro

# Create your views here.
menu = {"menu": ''}

redirectpagina = 'main:homepage'
shelados = shelados.objects.all()
spizza = spizza.objects.all()
usuario=usuarios.objects.all()
tpedido = Pedido.objects.all()
lineapedido = LineaPedido.objects.all()


def homepage(request):
    return render(request, 'main/index.html', {"shelado": shelados, "spizza": spizza, "usu": usuario})


def carta(request):
    return render(request, 'main/Menu/menu.html', {"shelado": shelados, "spizza": spizza, "usu": usuario})


def heladeria(request):
    global redirectpagina
    redirectpagina = request.path_info
    productos = producto.objects.all()
    return render(request, 'main/Menu/Helados.html', {"productos": productos, "shelado": shelados, "spizza": spizza, "usu": usuario})


def comrapida(request):
    global redirectpagina
    redirectpagina = request.path_info
    productos = producto.objects.all()
    return render(request, 'main/Menu/Comidas_rapidas.html', {"productos": productos, "shelado": shelados, "spizza": spizza, "usu": usuario})


def pizzeria(request):
    global redirectpagina
    redirectpagina = request.path_info
    productos = producto.objects.all()
    return render(request, 'main/Menu/pizza.html', {"productos": productos, "shelado": shelados, "spizza": spizza, "usu": usuario})


def bebidas(request):
    global redirectpagina
    redirectpagina = request.path_info
    productos = producto.objects.all()
    return render(request, 'main/Menu/bebidas/Bebidas.html', {"productos": productos, "shelado": shelados, "spizza": spizza, "usu": usuario})


def galeria(request):
    return render(request, 'main/galeria/index.html', {"shelado": shelados, "spizza": spizza, "usu": usuario})


def domicilios(request):
    return render(request, 'main/Menu/menu.html', {"shelado": shelados, "spizza": spizza, "usu": usuario})

def perfil(request):
    return render(request, 'main/Perfil/Perfil.html', {"usu": usuario})

def pedidos(request):
    return render(request, 'main/Pedidos/Pedidos.html', {"tpedido": tpedido, "lineapedido": lineapedido})


def login(request):
    if request.user.is_authenticated:
        messages.error(request, "Ya esta logeado")
        return redirect('main:homepage')
    if request.POST:
        username = request.POST.get('username')
        contra = request.POST.get('pass')
        user = authenticate(request, username=username, password=contra)
        if user is not None:
            login_auth(request, user)
            messages.success(request, f"Estas logeado como {username}")
            return redirect('main:homepage')
        else:
            messages.error(request, "Usuario o Contraseña Erronea")
            return redirect('main:login')

    return render(request, 'main/Login-Register/login/login.html')


def logout_request(request):
    logout(request)
    messages.info(request, "Cerraste Sesion Exitosamente")

    return redirect('main:homepage')


def register(request):
    if request.user.is_authenticated:
        messages.error(request, "Ya esta logeado")
        return redirect('main:homepage')
    if request.POST:
        username = request.POST.get('username')
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        email = request.POST.get('email')
        celular = request.POST.get('celular')
        direc = request.POST.get('direccion')
        pasw = request.POST.get('contraseña')
        contraseña = make_password(pasw)
        if User.objects.filter(username=username).exists():
            messages.error(request, "Este Usuario ya Existe")
            return redirect('main:register')
        else:
            user = User(
                username=username,
                email=email,
                password=contraseña
            )
            user.save()

            new_user = usuarios(
                usuario=user,
                nombre=nombre,
                apellidos=apellidos,
                email=email,
                celular=celular,
                direccion=direc,
                contraseña=pasw
            )
            new_user.save()
            login_auth(request, user)
            messages.success(request, f"Cuenta creada Exitosamente")

            return redirect('main:homepage')

    return render(request, 'main/Login-Register/register/register.html')


# |-----------------------------------Carrito---------------------------------------|

def agregar_producto(request, producto_id):
    #pagina = request.path.get()
    # print(pagina)
    carro = Carro(request)
    pproducto = producto.objects.get(id=producto_id)
    carro.agregar(producto=pproducto)
    return redirect(redirectpagina)


def eliminar_producto(request, producto_id):
    carro = Carro(request)
    pproducto = producto.objects.get(id=producto_id)
    carro.eliminar(producto=pproducto)
    return redirect(redirectpagina)


def restar_producto(request, producto_id):
    carro = Carro(request)
    pproducto = producto.objects.get(id=producto_id)
    carro.restar_producto(producto=pproducto)
    return redirect(redirectpagina)


def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect(redirectpagina)

# |-----------------------------------Pedido---------------------------------------|

def procesar_pedido(request):
    total_car = importe_total_carro(request)
    pedido=Pedido.objects.create(user=request.user, total_ped =total_car["importe_total_carro"])
    carro=Carro(request)
    lineas_pedido=list()
    for key,value in carro.carro.items():
        lineas_pedido.append(LineaPedido(

                producto_id=key,
                cantidad=value["cantidad"],
                user=request.user,
                pedido=pedido

            ))

    LineaPedido.objects.bulk_create(lineas_pedido)
    limpiar_carro(request)

    messages.success(request, f"Pedido Creado Exitosamente")

    return redirect('main:homepage')

def eliminar_pedido(request, pedido_id):
    ttpedido = Pedido.objects.get(id=pedido_id)
    ttpedido.delete()
    messages.success(request, f"Pedido Realizado exitosamente")
    return redirect('main:homepage')
