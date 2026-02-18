from unittest.mock import patch
from django.core.cache import cache
from controle_veiculos.cambio import obter_cotacao_usd_brl_com_cache


def test_cotacao_usa_cache():
    with patch("controle_veiculos.cambio.cache.get") as mock_get, \
         patch("controle_veiculos.cambio.cache.set") as mock_set, \
         patch("controle_veiculos.cambio.obter_cotacao_usd_brl") as mock_func:

        mock_get.return_value = 5.2

        valor = obter_cotacao_usd_brl_com_cache()

        mock_func.assert_not_called()
        mock_set.assert_not_called()
        assert valor == 5.2