from django.forms import ModelForm
from django import forms
from .models import InventarioSoporte, Tareas, VacanteActivas, Ubicaciones,SolicitudEmpleo,Noticias,Procesos
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

class TaskForm(ModelForm):
    class Meta:
        model = Tareas
        fields = ['title', 'descrpcion','importante']

class VacantesAForm(ModelForm):
    class Meta:
        model = VacanteActivas
        fields = ['vacante', 'descripcion','departamento', 'respon','sueldo' , 'estatus']
        
class UbicacionesForm(ModelForm):
    class Meta:
        model = Ubicaciones
        fields = ['ubicacion', 'empresa','codigo_sucursal','telefono','extension','nombre_tiular','ap_paterno','email','direccion','tipo_cedis','coordenadas']
        
class SolicitudEmpleoForm(ModelForm):
    
    class Meta:
        model = SolicitudEmpleo
        fields = ['puesto','nombres','ap_paterno','ap_materno','escolaridad','correo','numero','likedin','experiencia','curriculum']

class NoticiasForm(ModelForm):
    
    class Meta:
        model = Noticias
        fields = ['titulo','imagen','descripcion','fecha_noticia','tipo_noticia','empresa','user']
class ProcesosForm(ModelForm):
    
    class Meta:
        model = Procesos
        fields = ['titulo','descripcion','documento','departamento','empresa','tipo_documento']