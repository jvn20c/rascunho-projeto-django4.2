from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from contas import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('animais.urls')),
    path('cadastro/', user_views.register, name="user-register"),
    # novas urls
    path('entrar/', auth_views.LoginView.as_view(
        template_name='contas/entrar.html'),
        name="user-login"),
    path('sair/', auth_views.LogoutView.as_view(
        template_name='contas/sair.html'),
        name="user-logout"),
    path('perfil/', user_views.perfil, name="user-profile"),
]
