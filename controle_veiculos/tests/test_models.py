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

@pytest.mark.django_db
def test_soft_delete_nao_remove_do_banco():
    v = Veiculo.objects.create(
        placa="XYZ9876",
        marca="Toyota",
        modelo="Corolla",
        ano=2021,
        cor="Prata",
        preco_usd=20000
    )

    v.ativo = False
    v.save()

    assert Veiculo.objects.filter(id=v.id).exists()

@pytest.mark.django_db
def test_consulta_padrao_nao_retorna_inativos():
    Veiculo.objects.create(
        placa="AAA1111",
        marca="Honda",
        modelo="Civic",
        ano=2020,
        cor="Azul",
        preco_usd=18000,
        ativo=True
    )

    Veiculo.objects.create(
        placa="BBB2222",
        marca="Honda",
        modelo="Fit",
        ano=2019,
        cor="Preto",
        preco_usd=12000,
        ativo=False
    )

    ativos = Veiculo.objects.ativos()

    assert ativos.count() == 1
