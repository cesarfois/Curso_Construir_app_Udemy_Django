from django import forms
from .models import Registrado

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields =['nome', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, proveedor = email.split('@')
        dominio, extension = proveedor.split('.')
        if not extension == 'edu':
            raise forms.ValidationError('Por favor utiliza com final .EDU')
        return email

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        #validadiones
        return nome


class RegForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()