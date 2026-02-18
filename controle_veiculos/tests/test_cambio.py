import pytest
from unittest.mock import patch
from controle_veiculos.cambio import obter_cotacao_usd_brl

def test_cotacao_usd_brl_api_principal():
    with patch("controle_veiculos.cambio.requests.get") as mock_get:
        mock_get.return_value.json.return_value = {
            "USDBRL": {"bid": "5.00"}
        }
        mock_get.return_value.status_code = 200

        valor = obter_cotacao_usd_brl()
        assert valor == 5.0

def test_cotacao_usd_brl_fallback():
    with patch("controle_veiculos.cambio.requests.get") as mock_get:
        mock_get.side_effect = Exception("API principal caiu")

        with patch("controle_veiculos.cambio.requests.get") as mock_fallback:
            mock_fallback.return_value.json.return_value = {
                "rates": {"BRL": 5.1}
            }
            mock_fallback.return_value.status_code = 200

            valor = obter_cotacao_usd_brl()
            assert valor == 5.1