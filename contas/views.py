from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from . import forms

# Create your views here.


def register(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # cleaned data é um dictionary
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"{username}, sua conta foi criada, por favor entre!")
            return redirect('user-login')
    else:
        form = forms.UserRegisterForm()
    return render(request, 'contas/registro.html', {'form': form})


@login_required()
def perfil(request):
    return render(request, 'contas/perfil.html')
