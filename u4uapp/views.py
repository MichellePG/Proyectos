from django.shortcuts import render, redirect
from u4uapp.models import Universidad, Carrera, Comentario, Carreraesp
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from u4uapp.forms import NuevoComentarioModelForm

def home(request):
    if request.method == "GET":
        return render(request, "u4uapp/homepage.html")

def universidades(request):
    universidades = Universidad.objects.all()
    if request.method == "GET":
        return render(request, "u4uapp/universidades.html", {"universidades": universidades})
    elif request.method == "POST":
        if "aplicarBusqueda" in request.POST:
            # guardamos el contenido de la busqueda en una variable query
            query = request.POST["busqueda"]
            # guardamos en universidades solo las universidades donde query es substring del nombre
            universidades = universidades.filter(nombre__icontains=query)
            # renderiamos nuevamente la pagina con la lista reducida de universidades
            return render(request, "u4uapp/universidades.html", {"universidades": universidades})

def universidad(request, universidad_id):
    universidad = Universidad.objects.get(id=universidad_id)
    # funcionalidad de ManyToMany permite obtener todas las carreras impartidas por una universidad
    carreras = universidad.carrera_set.all()
    comentarios = Comentario.objects.filter(universidad=universidad)
    if request.method == "GET":
        form_comentario = NuevoComentarioModelForm()
        return render(request, "u4uapp/universidad.html", {"universidad": universidad, "carreras": carreras, "form_comentario": form_comentario, "comentarios": comentarios})
    elif request.method == "POST":
        form_comentario = NuevoComentarioModelForm(request.POST)
        if form_comentario.is_valid():
            nuevo_comentario = form_comentario.save(commit=False)
            nuevo_comentario.universidad = universidad
            if request.user.is_authenticated:
                nuevo_comentario.autor = request.user
                nuevo_comentario.save()
        return render(request, "u4uapp/universidad.html", {"universidad": universidad, "carreras": carreras, "form_comentario": form_comentario, "comentarios": comentarios})

def carreras(request):
    carreras = Carrera.objects.all()
    if request.method == "GET":
        return render(request, "u4uapp/carreras.html", {"carreras": carreras})
    elif request.method == "POST":
        if "aplicarBusqueda" in request.POST:
            # guardamos el contenido de la busqueda en una variable query
            query = request.POST["carreras_busqueda"]
            # guardamos en carreras solo las carreras donde query es substring del nombre
            carreras = carreras.filter(nombre__icontains=query)
            # renderiamos nuevamente la pagina con la lista reducida de carreras
            return render(request, "u4uapp/carreras.html", {"carreras": carreras})

def carrera(request, carrera_id):
    carrera = Carrera.objects.get(id=carrera_id)
    # funcionalidad de ManyToMany permite obtener todas las universidades que imparten una carrera
    universidades = carrera.universidades.all()
    if request.method == "GET":
        return render(request, "u4uapp/carrera.html", {"carrera": carrera, "universidades": universidades})

def carreraesp(request, carreraesp_id):
    carreraesp = Carreraesp.objects.get(id=carreraesp_id)
    #
    if request.method == "GET":
        return render(request, "u4uapp/carreraesp.html", {"carreraesp": carreraesp})


def registrar_usuario(request):
    if request.method == "GET":
        return render(request, "u4uapp/registrar_usuario.html")
    elif request.method == "POST":
        nombre_usuario = request.POST['nombre_usuario']
        e_mail = request.POST['e-mail']
        contrasena = request.POST['contrasena']
        
        user = User.objects.create_user(username=nombre_usuario, password=contrasena, email=e_mail)
        return render(request, "u4uapp/homepage.html")

def iniciar_sesion(request):
    if request.method == "GET":
        return render(request, "u4uapp/iniciar_sesion.html")
    elif request.method == "POST":
        nombre_usuario = request.POST['nombre_usuario']
        contrasena = request.POST['contrasena']
        usuario = authenticate(username=nombre_usuario, password=contrasena)
        if usuario is not None:
            login(request, usuario)
            return render(request, "u4uapp/homepage.html")
        return render(request, "u4uapp/iniciar_sesion.html")

def cerrar_sesion(request):
    logout(request)
    return render(request, "u4uapp/homepage.html")
