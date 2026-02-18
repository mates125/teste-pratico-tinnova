import pytest
from django.urls import reverse
from conftest import user_token, admin_token, api_client
from controle_veiculos.models import Veiculo

@pytest.mark.django_db
def test_put_veiculo_com_user_retorna_403(api_client, user_token):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user_token}")

    v = Veiculo.objects.create(
        placa="GGG7777",
        marca="Ford",
        modelo="Ka",
        ano=2020,
        cor="Preto",
        preco_usd=10000
    )

    url = reverse("veiculos-detail", args=[v.id])
    response = api_client.put(url, {"marca": "Fiat"}, format="json")

    assert response.status_code == 403

@pytest.mark.django_db
def test_put_veiculo_com_admin_retorna_200(api_client, admin_token):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {admin_token}")

    v = Veiculo.objects.create(
        placa="HHH8888",
        marca="Ford",
        modelo="Ka",
        ano=2020,
        cor="Preto",
        preco_usd=10000
    )

    url = reverse("veiculos-detail", args=[v.id])
    response = api_client.put(
        url,
        {
            "placa": "HHH8888",
            "marca": "Fiat",
            "modelo": "Uno",
            "ano": 2021,
            "cor": "Branco",
            "preco_usd": 9000
        },
        format="json"
    )

    assert response.status_code == 200

@pytest.mark.django_db
def test_patch_veiculo_atualiza_parcialmente(api_client, admin_token):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {admin_token}")

    v = Veiculo.objects.create(
        placa="III9999",
        marca="Ford",
        modelo="Ka",
        ano=2020,
        cor="Preto",
        preco_usd=10000
    )

    url = reverse("veiculos-detail", args=[v.id])
    response = api_client.patch(url, {"cor": "Azul"}, format="json")

    assert response.status_code == 200
