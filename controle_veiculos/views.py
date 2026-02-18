from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from django.db.models import Count
from controle_veiculos.models import Veiculo

class VeiculoListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        filtros = {
            "id": request.query_params.get("id"),
            "placa": request.query_params.get("placa"),
            "marca": request.query_params.get("marca"),
            "modelo": request.query_params.get("modelo"),
            "ano": request.query_params.get("ano"),
            "cor": request.query_params.get("cor"),
            "min_preco": request.query_params.get("minPreco"),
            "max_preco": request.query_params.get("maxPreco"),
        }

        veiculos = Veiculo.objects.filtrar(
            id=filtros["id"],
            placa=filtros["placa"],
            marca=filtros["marca"],
            modelo=filtros["modelo"],
            ano=filtros["ano"],
            cor=filtros["cor"],
            min_preco=filtros["min_preco"],
            max_preco=filtros["max_preco"],
        )

        data = [
            {
                "id": v.id,
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

    def put(self, request, pk):
        if not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)

        veiculo = get_object_or_404(Veiculo, pk=pk)

        for campo in ["placa", "marca", "modelo", "ano", "cor", "preco_usd"]:
            setattr(veiculo, campo, request.data.get(campo))

        veiculo.save()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, pk):
        if not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)

        veiculo = get_object_or_404(Veiculo, pk=pk)

        for campo, valor in request.data.items():
            setattr(veiculo, campo, valor)

        veiculo.save()
        return Response(status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        if not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)

        veiculo = get_object_or_404(Veiculo, pk=pk)
        veiculo.ativo = False
        veiculo.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

class VeiculosRelatorioPorMarcaView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        qs = (
            Veiculo.objects.ativos()
            .values("marca")
            .annotate(total=Count("id"))
        )

        data = {item["marca"]: item["total"] for item in qs}
        return Response(data)