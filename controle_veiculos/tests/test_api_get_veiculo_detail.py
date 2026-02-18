import pytest
from django.urls import reverse
from conftest import user_token, admin_token, api_client
from controle_veiculos.models import Veiculo

@pytest.mark.django_db
def test_get_veiculo_por_id_retorna_200(api_client, user_token):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user_token}")

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
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.json()["placa"] == "CCC3333"

@pytest.mark.django_db
def test_get_veiculo_inexistente_retorna_404(api_client, user_token):
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {user_token}")

    url = reverse("veiculos-detail", args=[999])
    response = api_client.get(url)

    assert response.status_code == 404