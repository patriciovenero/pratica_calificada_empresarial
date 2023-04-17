from django.shortcuts import render
from .models import pregunta, respuesta
# Create your views here.
def index(request):
    lista_entrega = pregunta.objects.all()
    context= {
        pregunta:lista_entrega
    }
    return render(request,'index.html',context)

def registro(request):
    data_nombre = request.POST['nombre']
    data_email = request.POST['email']


    objAlumno = data_nombre.objects.create(
        nombre = data_nombre,
        email = data_email
    )

    objnombre = data_nombre()
    objnombre.alumno = objnombre
    objnombre.emial = int(data_nombre)
    objnombre.save()

    context = {
        'notas' :data_email.objects.all()
    }

    return render(request, 'posiciones.html',context)
