from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect, render
from personas.models import Persona

# Create your views here.
def detallePersona(request, id):
    persona = Persona.objects.get(pk=id)
    #OTRA FORMA DE IMPORTAR CON ERROR 404
    # persona = get_object_or_404(Persona, pk=id)
    # y la importamos despues de render: render, get_object_or_404
    return render(request, 'personas/detalle.html', {'persona': persona})

PersonaForm = modelform_factory(Persona, exclude=[])

#agregando una nueva persona
def nuevaPersona(request):
    #esto se hace para recibir la informacion que se proporciona la pagina.
    if request.method == "POST":
        formaPersona = PersonaForm(request.POST)
        #aqui validamos el formulario.
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm()

    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})


#editando una lista de personas
def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == "POST":
        formaPersona = PersonaForm(request.POST, instance=persona)
        #aqui validamos el formulario.
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        persona = get_object_or_404(Persona, pk=id)
        formaPersona = PersonaForm(instance=persona)

    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})


#eliminamos una persona simplemente con el metodo .delete()
def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('index')

    