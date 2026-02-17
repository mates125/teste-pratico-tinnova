import pytest
from controle_veiculos.models import Veiculo

@pytest.mark.django_db
def test_nao_permite_placa_duplicada():
    Veiculo.objects.create(
        placa="ABC1234",
        marca="Ford",
        modelo="Ka",
        ano=2020,
        cor="Preto",
        preco_usd=10000
    )

    with pytest.raises(Exception):
        Veiculo.objects.create(
            placa="ABC1234",
            marca="Fiat",
            modelo="Uno",
            ano=2019,
            cor="Branco",
            preco_usd=9000
        )
