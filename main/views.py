from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as login_auth
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import usuarios, producto
from django.shortcuts import render, redirect
from .carro import Carro

# Create your views here.
menu = {"menu": ''}


def homepage(request):
    return render(request, 'main/index.html')


def carta(request):
    return render(request, 'main/Menu/menu.html')


def heladeria(request):
    productos = producto.objects.all()
    return render(request, 'main/Menu/Helados.html', {"productos": productos})


def comrapida(request):
    productos = producto.objects.all()
    return render(request, 'main/Menu/Comidas_rapidas.html', {"productos": productos})


def pizzeria(request):
    productos = producto.objects.all()
    return render(request, 'main/Menu/pizza.html', {"productos": productos})


def bebidas(request):
    productos = producto.objects.all()
    return render(request, 'main/Menu/bebidas/Bebidas.html', {"productos": productos})


def galeria(request):
    return render(request, 'main/galeria/index.html')


def domicilios(request):
    return render(request, 'main/Menu/menu.html')


def login(request):
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

    if request.POST:
        username = request.POST.get('username')
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        email = request.POST.get('email')
        celular = request.POST.get('celular')
        pasw = request.POST.get('contraseña')
        contraseña = make_password(pasw)

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
            contraseña=pasw
        )
        new_user.save()
        # entrar = authenticate(request, username=username, password=contraseña)
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
    return redirect('main:carta')


def eliminar_producto(request, producto_id):
    carro = Carro(request)
    pproducto = producto.objects.get(id = producto_id)
    carro.eliminar(producto=pproducto)
    return redirect('main:carta')


def restar_producto(request, producto_id):
    carro = Carro(request)
    pproducto = producto.objects.get(id=producto_id)
    carro.restar_producto(producto=pproducto)
    return redirect('main:carta')


def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect('main:carta')