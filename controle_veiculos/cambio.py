import requests
from django.core.cache import cache

API_PRINCIPAL = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
API_FALLBACK = "https://api.frankfurter.app/latest?from=USD&to=BRL"

def obter_cotacao_usd_brl():
    try:
        response = requests.get(API_PRINCIPAL, timeout=5)
        data = response.json()
        return float(data["USDBRL"]["bid"])
    except Exception:
        response = requests.get(API_FALLBACK, timeout=5)
        data = response.json()
        return float(data["rates"]["BRL"])
    
def obter_cotacao_usd_brl_com_cache():
    valor = cache.get("usd_brl")
    if valor:
        return valor

    valor = obter_cotacao_usd_brl()
    cache.set("usd_brl", valor, timeout=300)
    return valor
