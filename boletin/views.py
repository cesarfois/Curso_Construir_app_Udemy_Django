from django.conf import settings
from django.core.mail import send_mail

from django.shortcuts import render

from .forms import RegModelForm, ContactForm
from .models import Registrado

# Create your views here.

def inicio(request):
    titulo = "Bienvenidos"
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
    titulo = 'Contacto'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_mensaje = form.cleaned_data.get('mensaje')
        form_nome = form.cleaned_data.get('nome')
        asunto = 'form de contacto'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, 'otroemail@gmail.com']
        email_mensaje = '%s: %s enviado por %s' %(form_nome, form_mensaje, form_email)
        send_mail(
            asunto,
            email_mensaje,
            email_from,
            [email_to],
            fail_silently=False
            )

        '''-------Tercera forma --------------'''
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
        'titulo': titulo,
    }
    return render(request, 'forms.html', context)
