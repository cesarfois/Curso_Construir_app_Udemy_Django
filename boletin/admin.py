from django.contrib import admin
from .models import Registrado
from .forms import RegModelForm
# Register your models here.


class AdminRegistrado(admin.ModelAdmin):
    list_display = ['email', 'nome', 'timestamp']
    form = RegModelForm
    list_display_links = ['email']
    list_filter = ['timestamp']
    list_editable = ['nome']
    search_fields = ['nome', 'email']
    #class Meta:
    #    model = Registrado

admin.site.register(Registrado, AdminRegistrado)