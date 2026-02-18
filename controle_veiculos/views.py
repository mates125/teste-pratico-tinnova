from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from controle_veiculos.models import Veiculo
from django.shortcuts import get_object_or_404

class VeiculoListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        filtros = {
            "marca": request.query_params.get("marca"),
            "ano": request.query_params.get("ano"),
            "cor": request.query_params.get("cor"),
            "min_preco": request.query_params.get("minPreco"),
            "max_preco": request.query_params.get("maxPreco"),
        }

        veiculos = Veiculo.objects.filtrar(
            marca=filtros["marca"],
            ano=filtros["ano"],
            cor=filtros["cor"],
            min_preco=filtros["min_preco"],
            max_preco=filtros["max_preco"],
        )

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

class VeiculoDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        veiculo = get_object_or_404(Veiculo.objects.ativos(), pk=pk)

        return Response({
            "placa": veiculo.placa,
            "marca": veiculo.marca,
            "modelo": veiculo.modelo,
            "ano": veiculo.ano,
            "cor": veiculo.cor,
            "preco_usd": float(veiculo.preco_usd),
        })