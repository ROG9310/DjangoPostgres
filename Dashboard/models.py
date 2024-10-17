from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tareas(models.Model):
    title = models.CharField(max_length=200)
    descrpcion = models.TextField(blank=True)
    creacion = models.DateTimeField(auto_now_add=True)
    fecha_termino = models.DateField(null=True)
    importante = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + ' - by ' + self.user.username 
 
class Vacantes(models.Model):
    vacante = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_termino = models.DateField(null=True)
    estatus = models.BooleanField(default=False)
    sueldo = models.CharField(max_length=100,null=True)
    respon = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    departamento = models.TextField(blank=True)
    def __str__(self):
        return self.vacante  

class VacanteActivas(models.Model):
    vacante = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    departamento = models.CharField(max_length=100,null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_termino = models.DateField(null=True)
    estatus = models.BooleanField(default=False)
    sueldo = models.CharField(max_length=100,null=True)
    respon = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    departamento = models.CharField(max_length=100)
    def __str__(self):
        return self.vacante + ' - ' + self.departamento


class Ubicaciones(models.Model):
    ubicacion = models.CharField(max_length=100)
    empresa = models.CharField(max_length=10)
    codigo_sucursal = models.CharField(max_length=10,null=True)
    telefono = models.CharField(max_length=10,null=True)
    extension = models.CharField(max_length=10,null=True)
    nombre_tiular = models.CharField(max_length=50,null=True)
    ap_paterno = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=100,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200)
    tipo_cedis = models.CharField(max_length=10,null=True)
    coordenadas =models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.ubicacion + ' - ' + self.nombre_tiular

class VacanteAct(models.Model):
    vacante = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    departamento = models.CharField(max_length=100,null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_termino = models.DateField(null=True)
    estatus = models.BooleanField(default=False)
    sueldo = models.CharField(max_length=100,null=True)
    respon = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    departamento = models.CharField(max_length=100)
    def __str__(self):
        return self.vacante + ' - ' + self.departamento
    
class Empresas(models.Model):
    empresa = models.CharField(max_length=50)
    def __str__(self):
        return self.empresa

class Cursos(models.Model):
    curso = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    imagen = models.CharField(max_length=100)
    empresa_curso = models.CharField(max_length=50)
    archivo = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.curso + ' - ' + self.empresa_curso
    
class SolicitudEmpleo(models.Model):
    puesto = models.CharField(max_length=100)
    nombres = models.CharField(max_length=80)
    ap_paterno = models.CharField(max_length=80)
    ap_materno = models.CharField(max_length=80)
    escolaridad = models.CharField(max_length=80)
    correo = models.CharField(max_length=100)
    numero = models.CharField(max_length=15)
    likedin = models.CharField(max_length=255)
    experiencia = models.TextField(blank=True)
    curriculum =models.FileField(upload_to='filesPDF/CV/')
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombres + ' - ' + self.puesto
    
class Departamentos(models.Model):
    departamento =models.CharField(max_length=100)
    def __str__(self):
        return self.departamento 
class Puestos(models.Model):
    puesto =models.CharField((""), max_length=100)
    def __str__(self):
        return self.puesto
class UsuariosGA(models.Model):
    nombres = models.CharField(max_length=80)
    ap_paterno = models.CharField(max_length=80)
    ap_materno = models.CharField(max_length=80)
    empresa = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    sucursal = models.CharField(max_length=80)
    departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)
    puesto = models.ForeignKey(Puestos, on_delete=models.CASCADE)
    ap_materno = models.CharField(max_length=80)
    correo = models.CharField(max_length=100)
    extension = models.CharField(max_length=5)
    fecha_nacimiento= models.DateField(null=True)
    fecha_ingreso = models.DateField(null=True)
    rfc =models.CharField(max_length=13)
    numero_empleado=models.BigIntegerField
    foto =models.ImageField(upload_to='FotosPlantilla')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombres + ' - ' + self.puesto + ' - ' + self.empresa
    
    
    