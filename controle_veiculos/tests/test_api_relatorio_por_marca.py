import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from controle_veiculos.models import Veiculo

@pytest.mark.django_db
def test_relatorio_por_marca_retorna_quantidades(client):
    user = User.objects.create_user(username="user", password="123")
    client.force_login(user)

    Veiculo.objects.create(
        placa="REL0001", marca="Ford", modelo="Ka", 
        ano=2020, cor="Preto", preco_usd=10000, ativo=True
    )
    Veiculo.objects.create(
        placa="REL0002", marca="Ford", modelo="Fiesta", 
        ano=2019, cor="Branco", preco_usd=9000, ativo=True
    )
    Veiculo.objects.create(
        placa="REL0003", marca="Fiat", modelo="Uno", 
        ano=2018, cor="Vermelho", preco_usd=8000, ativo=True
    )
    Veiculo.objects.create(
        placa="REL0004", marca="Fiat", modelo="Mobi", 
        ano=2021, cor="Azul", preco_usd=11000, ativo=False
    )

    url = reverse("veiculos-relatorio-por-marca")
    response = client.get(url)

    assert response.status_code == 200
    data = response.json()

    assert data["Ford"] == 2
    assert data["Fiat"] == 1
