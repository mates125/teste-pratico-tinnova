import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from controle_veiculos.models import Veiculo

@pytest.mark.django_db
def test_put_veiculo_com_user_retorna_403(client):
    user = User.objects.create_user(username="user", password="123")
    client.force_login(user)

    v = Veiculo.objects.create(
        placa="GGG7777",
        marca="Ford",
        modelo="Ka",
        ano=2020,
        cor="Preto",
        preco_usd=10000
    )

    url = reverse("veiculos-detail", args=[v.id])
    response = client.put(url, {"marca": "Fiat"}, content_type="application/json")

    assert response.status_code == 403

@pytest.mark.django_db
def test_put_veiculo_com_admin_retorna_200(client):
    admin = User.objects.create_superuser(
        username="admin", password="123", email="admin@test.com"
    )
    client.force_login(admin)

    v = Veiculo.objects.create(
        placa="HHH8888",
        marca="Ford",
        modelo="Ka",
        ano=2020,
        cor="Preto",
        preco_usd=10000
    )

    url = reverse("veiculos-detail", args=[v.id])
    response = client.put(
        url,
        {
            "placa": "HHH8888",
            "marca": "Fiat",
            "modelo": "Uno",
            "ano": 2021,
            "cor": "Branco",
            "preco_usd": 9000
        },
        content_type="application/json"
    )

    assert response.status_code == 200

@pytest.mark.django_db
def test_patch_veiculo_atualiza_parcialmente(client):
    admin = User.objects.create_superuser(
        username="admin", password="123", email="admin@test.com"
    )
    client.force_login(admin)

    v = Veiculo.objects.create(
        placa="III9999",
        marca="Ford",
        modelo="Ka",
        ano=2020,
        cor="Preto",
        preco_usd=10000
    )

    url = reverse("veiculos-detail", args=[v.id])
    response = client.patch(
        url,
        {"cor": "Azul"},
        content_type="application/json"
    )

    assert response.status_code == 200