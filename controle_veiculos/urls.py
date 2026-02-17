from django.urls import path
from .views import VeiculoListView

urlpatterns = [
    path("veiculos/", VeiculoListView.as_view(), name="veiculos-list"),
]
