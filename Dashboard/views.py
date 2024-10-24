from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm, VacantesAForm,UbicacionesForm,SolicitudEmpleoForm
from .models import Tareas, VacanteActivas,Cursos,InventarioSoporte,Ubicaciones
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def Index(request):
    #return HttpResponse("<h1>Hola Mundo</h1>") #Para linea directa de djnago
    return render(request, "index.html",{
    }) 

@login_required
def createTarea(request):
    if request.method == 'GET':
        return render(request, "Create_task.html",{
            'form': TaskForm
        }) 
    else:
        try:
            form = TaskForm(request.POST)
            new_task =form.save(commit=False)
            new_task.user=request.user
            new_task.save()
            return redirect('tareas')
        except ValueError:
            return render(request, "Create_task.html",{
                'form': TaskForm,
                'error': 'Checar datos ingresados'
            }) 
            
def bolsa_trabajo(request):
    if request.method == 'GET':
        return render(request, "Solicitud_empleo.html", {
            'form': SolicitudEmpleoForm()
        })
    else:
        try:
            # Pasar tanto request.POST como request.FILES al formulario
            form = SolicitudEmpleoForm(request.POST, request.FILES)

            if form.is_valid():  # Validar el formulario antes de guardar
                nueva_solicitud = form.save(commit=False)  # Crear objeto pero no guardar aún
                if 'curriculum' in request.FILES:
                    nueva_solicitud.curriculum = request.FILES['curriculum']  # Asignar archivo
                nueva_solicitud.save()  # Guardar objeto en la base de datos
                return redirect('about_us')  # Redireccionar tras éxito
            else:
                # Si el formulario no es válido, renderizar el formulario con errores
                return render(request, "Solicitud_empleo.html", {
                    'form': form,
                    'error': 'Datos ingresados no son válidos, por favor revisa.'
                })
        except ValueError:
            return render(request, "Solicitud_empleo.html", {
                'form': SolicitudEmpleoForm(),
                'error': 'Ocurrió un error inesperado. Verifica tus datos.'
            })
  
def signup(request):
    if request.method == 'GET':
           return render(request, 'signup.html',{
                'form' : UserCreationForm
            })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Register User
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('tareas')
            except IntegrityError:
                return render(request, 'signup.html',{
                    'form' : UserCreationForm,
                    'error' : 'Usuario ya existe'
                })
                
        else:
            return render(request, 'signup.html',{
                'form' : UserCreationForm,
                'error' : 'Password no coincide'
            })

@login_required
def tareas(request):
    tareas = Tareas.objects.all()
    return render(request,'tareas.html',{
        'tareas' : tareas
    })


def signout(request):
    logout(request)
    return redirect('index')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request,username=request.POST['username'], password=request.POST['password'])
        username = username=request.POST['username']
        if user is None:
           return render(request, 'signin.html',{
            'form': AuthenticationForm,
            'error': 'Username o Password es incorrecto'
            })
           
        else:
            domain = username.split('@')[1]
            login(request,user)              
            if domain == 'alvamex.com.mx' or domain == 'vastro.com.mx' or domain == 'imex.com.mx' or domain == 'admin':
                return redirect('alvamex')
            elif domain == 'diamante.com.mx':
                return redirect('diamante')
            elif domain == 'tradepolymers.com.mx':
                return redirect('trade-polymers')
            elif domain == 'alvaenvases.com.mx':
                return redirect('alvaenvases')
            else:
                return render(request, 'signin.html',{
                'form': AuthenticationForm,
                'error': 'Username o Password es incorrecto'
                })

            

            
def about_us(request):
    return render(request,'about_us.html',{
    })
            
@login_required       
def empresa(request):
    messages.success(request, f'¡Bienvenid@, {request.user.first_name} {request.user.last_name}!')
    return render(request,'empresa.html',{
    })
    
@login_required   
def cedis(request):
    cedis = Ubicaciones.objects.filter(empresa = 'Alvamex')
    return render(request,'cedis.html',{'cedis': cedis
    })

@login_required              
def promociones(request):
    vacantes = VacanteActivas.objects.filter(estatus=0).select_related('user')
    return render(request,'promo.html',{
        'vacantes' : vacantes 
    })
    
@login_required
def procesos(request):    
    return render(request,'procesos.html',{
    })
    
@login_required
def dintranet(request):
    messages.success(request, f'¡Bienvenid@, {request.user.first_name} {request.user.last_name}!')
    return render(request,'dintranet.html',{
    })
    
@login_required
def duniversidad(request):
    cursos = Cursos.objects.all().select_related('user')
    return render(request,'duniversidad.html',{
        'cursos' : cursos
    })
    
@login_required
def dcedis(request):
    return render(request,'dcedis.html',{
    })
    
@login_required
def dprocesos(request):
    return render(request,'dprocesos.html',{
    })

@login_required    
def tradepolymers(request):
    messages.success(request, f'¡Bienvenid@, {request.user.first_name} {request.user.last_name}!')
    return render(request,'trade_polymers.html',{
    })

@login_required  
def promo(request):
    return render(request,'promociones.html',{ 
    })

@login_required     
def VacantesActivas(request):
    if request.method == 'GET':
        return render(request, "Crear_Proms.html",{
            'form': VacantesAForm
        }) 
    else:
        try:
            form = VacantesAForm(request.POST)
            new_task =form.save(commit=False)
            new_task.user=request.user
            new_task.save()
            return redirect('promociones')
        except ValueError:
            return render(request, "Crear_proms.html",{
                'form': VacantesAForm,
                'error': 'Checar datos ingresados'
            })  
            
@login_required     
def ubicacionesCedis(request):
    if request.method == 'GET':
        return render(request, "NuevaUbicacion.html",{
            'form': UbicacionesForm
        }) 
    else:
        try:
            form = UbicacionesForm(request.POST)
            new_ubicacion =form.save(commit=False)
            new_ubicacion.user=request.user
            new_ubicacion.save()
            return redirect('cedis')
        except ValueError:
            return render(request, "NuevaUbicacion.html",{
                'form': UbicacionesForm,
                'error': 'Checar datos ingresados'
            })     

@login_required
def universidad(request):
    cursos = Cursos.objects.all()
    print(cursos)
    return render(request,'universidad.html',{
        'cursos' : cursos
    })
    
    
@login_required
def dprom(request):
    return render(request,'dprom.html',{
    })


@login_required
def tprom(request):
    return render(request,'tprom.html',{
    })

@login_required
def tuniversidad(request):
    return render(request,'tuniversidad.html',{
    })
@login_required
def tcedis(request):
    return render(request,'tcedis.html',{
    })

@login_required
def tprocesos(request):
    return render(request,'tprocesos.html',{
    })
    
@login_required    
def alvaenvases(request):
    messages.success(request, f'¡Bienvenid@, {request.user.first_name} {request.user.last_name}!')
    return render(request,'alvaenvases.html',{
    })
@login_required
def aprom(request):
    return render(request,'aprom.html',{
    })
@login_required
def auniversidad(request):
    return render(request,'auniversidad.html',{
    })
@login_required
def acedis(request):
    return render(request,'acedis.html',{
    })
@login_required
def aprocesos(request):
    return render(request,'aprocesos.html',{
    })
@login_required
def inventarios(request):
    inventarios = InventarioSoporte.objects.all()
    return render(request,'inventario.html',{
       'inventarios' : inventarios
    })