from django.contrib import admin
from .models import Tareas, VacanteActivas, Ubicaciones,  Empresas, Cursos,SolicitudEmpleo,Puestos,Departamentos,UsuariosGA,Noticias,TipoNoticia
class TareaAdmin(admin.ModelAdmin):
    readonly_fields = ("creacion",)
    
    
admin.site.register(Tareas,TareaAdmin)


class UbicacionAdmin(admin.ModelAdmin):
    readonly_fields = ()
    
admin.site.register(Ubicaciones, UbicacionAdmin)


class VacanteActAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_creacion",)
    
admin.site.register(VacanteActivas, VacanteActAdmin)
class EmpresasAdmin(admin.ModelAdmin):
    readonly_fields = ()
    
admin.site.register(Empresas, EmpresasAdmin)

class CursosAdmin(admin.ModelAdmin):
    readonly_fields = ()
    
admin.site.register(Cursos, CursosAdmin)

class SolicitudEmpleosAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_solicitud",)
    
admin.site.register(SolicitudEmpleo, SolicitudEmpleosAdmin)

class PuestosAdmin(admin.ModelAdmin):
    readonly_fields = ()
    
admin.site.register(Puestos, PuestosAdmin)

class DepartamentosAdmin(admin.ModelAdmin):
    readonly_fields = ()
    
admin.site.register(Departamentos, DepartamentosAdmin)
class UsuariosGAAdmin(admin.ModelAdmin):
    readonly_fields = ()

class Tipo_NoticiaAdmin(admin.ModelAdmin):
    readonly_fields = ()
    
admin.site.register(TipoNoticia, Tipo_NoticiaAdmin)

class NoticiasAdmin(admin.ModelAdmin):
    readonly_fields = ()
    
admin.site.register(Noticias, NoticiasAdmin)
