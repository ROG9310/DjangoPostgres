from django.forms import ModelForm
from django import forms
from .models import Tareas, VacanteActivas, Ubicaciones,SolicitudEmpleo,Noticias, UsuariosGA,Procesos,TipoNoticia,TipoEquipos,TipoDiscoC,TipoDiscoD,TipoDocumento,DominiosRed,MarcaEquipos,MarcaEquiposMonitor,MarcaEquiposMouse,MarcaEquiposTeclado,MemoriasRam,VersionesOffice,InventarioSoporte


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


class UsuariosGAForm(ModelForm):
    
    class Meta:
        model = UsuariosGA
        fields = ['nombres','ap_paterno','ap_materno','empresa','sucursal','departamento','puesto','correo','extension','fecha_nacimiento','fecha_ingreso','rfc','numero_empleado','foto']
        
class TipoNoticiaForm(ModelForm):
    class Meta:
        model = TipoNoticia
        fields = ['tipo_noticia']
        

        
        
        
