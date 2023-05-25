from django.urls import path

from . import views

urlpatterns = [
    path('', views.AnimalListView.as_view(), name="animais-home"),
    path('animal/<int:pk>', views.AnimalDetailView.as_view(), name="animais-detalhes"),  # noqa E501
    path('animal/criar', views.AnimalCreateView.as_view(), name="animais-criar"),  # noqa E501
    path('animal/<int:pk>/editar', views.AnimalUpdateView.as_view(), name="animais-editar"),  # noqa E501
    path('animal/<int:pk>/excluir', views.AnimalDeleteView.as_view(), name="animais-excluir"),  # noqa E501
    path('sobre/', views.sobre, name="animais-sobre"),
]
