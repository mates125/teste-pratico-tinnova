from django.urls import path
from .views import VeiculoListView, VeiculoDetailView

urlpatterns = [
    path("veiculos/", VeiculoListView.as_view(), name="veiculos-list"),
    path("veiculos/<int:pk>/", VeiculoDetailView.as_view(), name="veiculos-detail"),
]
