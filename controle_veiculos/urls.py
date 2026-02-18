from django.urls import path
from .views import VeiculoListView, VeiculoDetailView, VeiculosRelatorioPorMarcaView

urlpatterns = [
    path("veiculos/", VeiculoListView.as_view(), name="veiculos-list"),
    path("veiculos/<int:pk>/", VeiculoDetailView.as_view(), name="veiculos-detail"),
    path("veiculos/relatorios/por-marca/", VeiculosRelatorioPorMarcaView.as_view(), name="veiculos-relatorio-por-marca"),
]