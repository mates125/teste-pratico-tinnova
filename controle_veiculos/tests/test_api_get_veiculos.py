import pytest
from django.urls import reverse
from controle_veiculos.models import Veiculo
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_get_veiculos_sem_auth_retorna_403(client):
    url = reverse("veiculos-list")
    response = client.get(url)
    assert response.status_code == 403

@pytest.mark.django_db
def test_get_veiculos_com_user_autenticado_retorna_200(client):
    user = User.objects.create_user(username="user", password="123")
    client.force_login(user)

    url = reverse("veiculos-list")
    response = client.get(url)

    assert response.status_code == 200

@pytest.mark.django_db
def test_get_veiculos_retorna_apenas_ativos(client):
    user = User.objects.create_user(username="user", password="123")
    client.force_login(user)

    Veiculo.objects.create(
        placa="AAA1111",
        marca="Ford",
        modelo="Ka",
        ano=2020,
        cor="Preto",
        preco_usd=10000,
        ativo=True
    )

    Veiculo.objects.create(
        placa="BBB2222",
        marca="Fiat",
        modelo="Uno",
        ano=2019,
        cor="Branco",
        preco_usd=9000,
        ativo=False
    )

    url = reverse("veiculos-list")
    response = client.get(url)

    assert len(response.json()) == 1