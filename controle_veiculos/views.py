from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from controle_veiculos.models import Veiculo
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from rest_framework import status

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

    def post(self, request):
        if not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)

        try:
            Veiculo.objects.create(
                placa=request.data["placa"],
                marca=request.data["marca"],
                modelo=request.data["modelo"],
                ano=request.data["ano"],
                cor=request.data["cor"],
                preco_usd=request.data["preco_usd"]
            )
        except IntegrityError:
            return Response(status=status.HTTP_409_CONFLICT)

        return Response(status=status.HTTP_201_CREATED)

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