import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from controle_veiculos.models import Veiculo

@pytest.mark.django_db
def test_post_veiculos_com_user_retorna_403(client):
    user = User.objects.create_user(username="user", password="123")
    client.force_login(user)

    payload = {
        "placa": "DDD4444",
        "marca": "Ford",
        "modelo": "Ka",
        "ano": 2020,
        "cor": "Preto",
        "preco_usd": 10000
    }

    url = reverse("veiculos-list")
    response = client.post(url, payload, content_type="application/json")

    assert response.status_code == 403

@pytest.mark.django_db
def test_post_veiculos_com_admin_retorna_201(client):
    admin = User.objects.create_superuser(
        username="admin", password="123", email="admin@test.com"
    )
    client.force_login(admin)

    payload = {
        "placa": "EEE5555",
        "marca": "Fiat",
        "modelo": "Uno",
        "ano": 2021,
        "cor": "Branco",
        "preco_usd": 9000
    }

    url = reverse("veiculos-list")
    response = client.post(url, payload, content_type="application/json")

    assert response.status_code == 201

@pytest.mark.django_db
def test_post_veiculos_placa_duplicada_retorna_409(client):
    admin = User.objects.create_superuser(
        username="admin", password="123", email="admin@test.com"
    )
    client.force_login(admin)

    Veiculo.objects.create(
        placa="FFF6666",
        marca="Ford",
        modelo="Ka",
        ano=2020,
        cor="Preto",
        preco_usd=10000
    )

    payload = {
        "placa": "FFF6666",
        "marca": "Fiat",
        "modelo": "Uno",
        "ano": 2019,
        "cor": "Branco",
        "preco_usd": 9000
    }

    url = reverse("veiculos-list")
    response = client.post(url, payload, content_type="application/json")

    assert response.status_code == 409