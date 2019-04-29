from django.shortcuts import render

from .forms import RegForm
from .models import Registrado

# Create your views here.

def inicio(request):
    titulo = "Hola"
    if request.user.is_authenticated:
        titulo = 'Bienvenido %s' %(request.user)
    form = RegForm(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        abc = form_data.get('email')
        cdg = form_data.get('nome')
        obj = Registrado.objects.create(email=abc, nome=cdg)
        ''' esto es lo mismo que ...
        obj = Registrado()
        obj.email = abc
        obj.save()
        
        '''
        
    context = {
        'el_titulo': titulo,
        'el_form': form,
    }
    return render(request, 'inicio.html', context)
