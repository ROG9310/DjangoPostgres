from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name="index"),
    path('about_us/', views.about_us, name="about_us"),
    path('tareas/create/', views.createTarea, name="create_task"),
    path('signup/', views.signup, name="singup"),
    path('tareas/', views.tareas, name="tareas"),
    path('logout/', views.signout, name="logout"),
    path('signin/', views.signin, name="signin"),
    path('alvamex/', views.empresa, name="alvamex"),
    path('cedis/', views.cedis, name="cedis"),
    path('cedis/nueva_Ubicacion/', views.ubicacionesCedis, name="nuevocedis"),
    path('promociones/', views.promociones, name="promociones"),
    path('promociones/SubirVacantes/', views.VacantesActivas, name="CrearPromociones"),
    path('procesos/', views.procesos, name="procesos"),
    path('diamante/dintranet/', views.dintranet, name="dintranet"),
    path('diamante/', views.dintranet, name="diamante"),
    path('diamante/duniversidad/', views.duniversidad, name="duniversidad"),
    path('diamante/dcedis/', views.dcedis, name="dcedis"),
    path('diamante/dprocesos/', views.dprocesos, name="dprocesos"),
    path('trade-polymers/', views.tradepolymers, name="trade-polymers"),
    path('promo/', views.promo, name="promo"),
    path('universidad/', views.universidad, name="universidad"),
    path('diamante/dprom/', views.dprom, name="promo"),
    path('trade-polymers/tprom/', views.tprom, name="tprom"),
    path('trade-polymers/tuniversidad/', views.tuniversidad, name="tuniversidad"),
    path('trade-polymers/tcedis/', views.tcedis, name="tcedis"),
    path('trade-polymers/tprocesos/', views.tprocesos, name="tprocesos"),
]
 