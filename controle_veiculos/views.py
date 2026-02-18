from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from controle_veiculos.models import Veiculo

class VeiculoListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        veiculos = Veiculo.objects.ativos()
        data = [
            {
                "placa": v.placa,
                "marca": v.marca,
                "modelo": v.modelo,
                "ano": v.ano,
                "cor": v.cor,
                "preco_usd": float(v.preco_usd),
            }
            for v in veiculos
        ]
        return Response(data)
