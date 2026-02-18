import pytest
from django.urls import reverse
from controle_veiculos.models import Veiculo
from conftest import user_token, admin_token, api_client

@pytest.mark.django_db
def test_get_veiculos_sem_auth_retorna_401(api_client):
    url = reverse("veiculos-list")
    response = api_client.get(url)
    assert response.status_code == 401

@pytest.mark.django_db
def test_get_veiculos_com_user_autenticado_retorna_200(api_client, user_token):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user_token}")

    url = reverse("veiculos-list")
    response = api_client.get(url)

    assert response.status_code == 200

@pytest.mark.django_db
def test_get_veiculos_retorna_apenas_ativos(api_client, user_token):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user_token}")

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
    response = api_client.get(url)

    assert len(response.json()) == 1

@pytest.mark.django_db
def test_get_veiculos_filtra_por_marca_e_ano(api_client, user_token):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user_token}")

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
        marca="Ford",
        modelo="Fiesta",
        ano=2019,
        cor="Branco",
        preco_usd=9000,
        ativo=True
    )

    url = reverse("veiculos-list") + "?marca=Ford&ano=2020"
    response = api_client.get(url)

    assert len(response.json()) == 1