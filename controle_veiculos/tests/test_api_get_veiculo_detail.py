import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from controle_veiculos.models import Veiculo

@pytest.mark.django_db
def test_get_veiculo_por_id_retorna_200(client):
    user = User.objects.create_user(username="user", password="123")
    client.force_login(user)

    v = Veiculo.objects.create(
        placa="CCC3333",
        marca="VW",
        modelo="Gol",
        ano=2021,
        cor="Cinza",
        preco_usd=11000,
        ativo=True
    )

    url = reverse("veiculos-detail", args=[v.id])
    response = client.get(url)

    assert response.status_code == 200
    assert response.json()["placa"] == "CCC3333"

@pytest.mark.django_db
def test_get_veiculo_inexistente_retorna_404(client):
    user = User.objects.create_user(username="user", password="123")
    client.force_login(user)

    url = reverse("veiculos-detail", args=[999])
    response = client.get(url)

    assert response.status_code == 404