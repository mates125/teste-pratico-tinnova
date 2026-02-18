import pytest
from django.urls import reverse
from controle_veiculos.models import Veiculo
from conftest import user_token, admin_token, api_client

@pytest.mark.django_db
def test_delete_veiculo_com_user_retorna_403(api_client, user_token):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user_token}")

    v = Veiculo.objects.create(
        placa="JJJ0001",
        marca="Ford",
        modelo="Ka",
        ano=2020,
        cor="Preto",
        preco_usd=10000
    )

    url = reverse("veiculos-detail", args=[v.id])
    response = api_client.delete(url)

    assert response.status_code == 403

@pytest.mark.django_db
def test_delete_veiculo_com_admin_realiza_soft_delete(api_client, admin_token):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {admin_token}")

    v = Veiculo.objects.create(
        placa="JJJ0002",
        marca="Fiat",
        modelo="Uno",
        ano=2019,
        cor="Branco",
        preco_usd=9000
    )

    url = reverse("veiculos-detail", args=[v.id])
    response = api_client.delete(url)

    v.refresh_from_db()

    assert response.status_code == 204
    assert v.ativo is False