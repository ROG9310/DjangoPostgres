from django.contrib import admin
from .models import Tareas, VacanteActivas, Ubicaciones, VacanteAct, Empresas

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