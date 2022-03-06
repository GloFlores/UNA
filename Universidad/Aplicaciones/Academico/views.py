from email import message
from django.shortcuts import redirect, render
from .models import Curso
from django.contrib import messages
# Create your views here.

def home (request):
    #Por la ORM QUE tiene Django, se podran listar los curso, por eso
    #Se importa el modelo Curso, y el modelo se hace objeto, llamando a todos los que seran cargados en el 
    #en una lista, asi con() se representa
    cursosListados= Curso.objects.all()
    
    #luego se envia entre llaves{}, 
    # #                                             !se va bajo el nombre cursos
    return render(request, "gestionCursos.html", {"cursos": cursosListados})

def registrarCurso(request):
    #EL POST que se manda debe tener relacion con el html que se quiere enviar, en cada campo
    codigo= request.POST['txtCodigo']
    nombre= request.POST['txtNombre']
    creditos= request.POST['numCreditos']
    
    curso= Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    
    messages.success(request,'Curso Registrado')
    #redirecciona a la ruta raiz 
    return redirect('/')
    
    
def edicionCurso(request,codigo):
    #listar datos
    curso= Curso.objects.get(codigo=codigo)
    #debe leer 1ro los cursos con render para luego editar
    return render(request,"edicionCurso.html",{"curso":curso})

def editarCurso(request):
    #debe tomar los 3 datos 
    codigo= request.POST['txtCodigo']
    nombre= request.POST['txtNombre']
    creditos= request.POST['numCreditos']
    
    curso= Curso.objects.get(codigo=codigo)    
    curso.nombre= nombre
    curso.creditos=creditos
    curso.save()
    messages.success(request,'Curso Modificado')
    return redirect('/')
    
    

def eliminarCurso(request,codigo):
    curso= Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request,'Curso Eliminado')
    return redirect('/')