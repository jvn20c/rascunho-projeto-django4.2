from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from . import models


class AnimalListView(ListView):
    model = models.Animal
    context_object_name = 'animais'
    ordering = ['-id']
    template_name = 'animais/home.html'

# Create your views here.


# def home(request):
#     animais = models.Animal.objects.all()
#     context = {
#         'animais': animais
#     }
#     return render(request, 'animais/home.html', context)


def sobre(request):
    return render(request, 'animais/sobre.html', {'titulo': 'página sobre'})


class AnimalDetailView(DetailView):
    model = models.Animal
    template_name_suffix = "_detalhes"


class AnimalDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Animal
    success_url = reverse_lazy('animais-home')

    def test_func(self):
        animal = self.get_object()
        return self.request.user == animal.autor


class AnimalCreateView(LoginRequiredMixin, CreateView):
    model = models.Animal
    fields = ['nome', 'descricao', 'data_nascimento']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class AnimalUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Animal
    fields = ['nome', 'descricao', 'data_nascimento']

    def test_func(self):
        animal = self.get_object()
        return self.request.user == animal.autor

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
