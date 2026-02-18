import pytest
from django.urls import reverse
from controle_veiculos.models import Veiculo
from conftest import user_token, admin_token, api_client

@pytest.mark.django_db
def test_post_veiculos_com_user_retorna_403(api_client, user_token):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user_token}")

    payload = {
        "placa": "DDD4444",
        "marca": "Ford",
        "modelo": "Ka",
        "ano": 2020,
        "cor": "Preto",
        "preco_usd": 10000
    }

    url = reverse("veiculos-list")
    response = api_client.post(url, payload, format="json")

    assert response.status_code == 403

@pytest.mark.django_db
def test_post_veiculos_com_admin_retorna_201(api_client, admin_token):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {admin_token}")

    payload = {
        "placa": "EEE5555",
        "marca": "Fiat",
        "modelo": "Uno",
        "ano": 2021,
        "cor": "Branco",
        "preco_usd": 9000
    }

    url = reverse("veiculos-list")
    response = api_client.post(url, payload, format="json")

    assert response.status_code == 201

@pytest.mark.django_db
def test_post_veiculos_placa_duplicada_retorna_409(api_client, admin_token):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {admin_token}")

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
    response = api_client.post(url, payload, format="json")

    assert response.status_code == 409