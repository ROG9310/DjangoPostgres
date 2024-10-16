from django.contrib import admin
from .models import Tareas, VacanteActivas, Ubicaciones,  Empresas, Cursos,SolicitudEmpleo
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