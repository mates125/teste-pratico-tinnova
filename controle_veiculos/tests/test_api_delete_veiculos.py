import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from controle_veiculos.models import Veiculo

@pytest.mark.django_db
def test_delete_veiculo_com_user_retorna_403(client):
    user = User.objects.create_user(username="user", password="123")
    client.force_login(user)

    v = Veiculo.objects.create(
        placa="JJJ0001",
        marca="Ford",
        modelo="Ka",
        ano=2020,
        cor="Preto",
        preco_usd=10000
    )

    url = reverse("veiculos-detail", args=[v.id])
    response = client.delete(url)

    assert response.status_code == 403

@pytest.mark.django_db
def test_delete_veiculo_com_admin_realiza_soft_delete(client):
    admin = User.objects.create_superuser(
        username="admin", password="123", email="admin@test.com"
    )
    client.force_login(admin)

    v = Veiculo.objects.create(
        placa="JJJ0002",
        marca="Fiat",
        modelo="Uno",
        ano=2019,
        cor="Branco",
        preco_usd=9000
    )

    url = reverse("veiculos-detail", args=[v.id])
    response = client.delete(url)

    v.refresh_from_db()

    assert response.status_code == 204
    assert v.ativo is False
