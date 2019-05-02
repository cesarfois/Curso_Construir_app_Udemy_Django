from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import Registrado

# Create your views here.

def inicio(request):
    titulo = "Hola"
    if request.user.is_authenticated:
        titulo = 'Bienvenido %s' %(request.user)
    form = RegModelForm(request.POST or None)

    context = {
        'el_titulo': titulo,
        'el_form': form,
    }


    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.nome:
            instance.nome = 'Pessoa'
        instance.save()

        context = {
            'el_titulo': 'Gracias %s!' % instance.nome
        }

        if not instance.nome:
            context = {
                "el_titulo": 'Gracias %s!' % instance.email
            }
        print(instance)
        print(instance.timestamp)


        #form_data = form.cleaned_data
        #abc = form_data.get('email')
        #cdg = form_data.get('nome')
        #obj = Registrado.objects.create(email=abc, nome=cdg)
        ''' esto es lo mismo que ...
        obj = Registrado()
        obj.email = abc
        obj.save()
        
        '''
        

    return render(request, 'inicio.html', context)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        for key, value in form.cleaned_data.items():
            print(key, value)

        '''-------Segunda forma --------------'''
        #for key in form.cleaned_data:
            #print(key)
            #print(form.cleaned_data.get(key))
        '''-------Primeira forma --------------'''
        #email = form.cleaned_data.get('email')
        #mensaje = form.cleaned_data.get('mensaje')
        #nome = form.cleaned_data.get('nome')
        #print(email, mensaje, nome)
    context = {
        'form' : form,
    }
    return render(request, 'forms.html', context)
