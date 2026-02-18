from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("veiculos")),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("veiculos/", views.veiculos_view, name="veiculos"),
    path("veiculos/<int:id>/", views.veiculo_detalhe_view, name="veiculo_detalhe"),
    path("veiculos/novo/", views.veiculo_novo_view, name="veiculo_novo"),
    path("veiculos/<int:id>/editar/", views.veiculo_editar_view, name="veiculo_editar"),
    path("veiculos/<int:id>/excluir/", views.veiculo_excluir_view, name="veiculo_excluir"),
]

