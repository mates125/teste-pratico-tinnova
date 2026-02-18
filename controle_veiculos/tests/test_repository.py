import pytest
from controle_veiculos.models import Veiculo

@pytest.mark.django_db
def test_filtro_combinado_marca_ano_cor():
    Veiculo.objects.create(
        placa="AAA0001",
        marca="Ford",
        modelo="Ka",
        ano=2020,
        cor="Preto",
        preco_usd=10000,
        ativo=True
    )
    Veiculo.objects.create(
        placa="BBB0002",
        marca="Ford",
        modelo="Fiesta",
        ano=2019,
        cor="Branco",
        preco_usd=9000,
        ativo=True
    )

    qs = Veiculo.objects.filtrar(
        marca="Ford",
        ano=2020,
        cor="Preto"
    )

    assert qs.count() == 1