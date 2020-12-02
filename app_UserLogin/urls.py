from django.urls import path, include
from . import views

urlpatterns = [
    #rendering paths
    path('', views.index),
    path('success', views.show_dashboard),

    #redirecting paths
    path('resgister', views.register_user),
    path('login', views.login_user),
    path('logout', views.logout)

]

