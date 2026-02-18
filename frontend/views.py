import requests
from django.shortcuts import render, redirect
from django.conf import settings

API_BASE_URL = "http://127.0.0.1:8000"

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        response = requests.post(
            f"{API_BASE_URL}/api/token/",
            json={"username": username, "password": password},
        )

        if response.status_code == 200:
            request.session["access_token"] = response.json()["access"]
            return redirect("veiculos")

        return render(request, "login.html", {"error": "Login inválido"})

    return render(request, "login.html")

def veiculos_view(request):
    token = request.session.get("access_token")
    if not token:
        return redirect("login")

    headers = {"Authorization": f"Bearer {token}"}

    params = {}
    for campo in ["marca", "modelo", "placa", "ano", "cor", "minPreco", "maxPreco"]:
        valor = request.GET.get(campo)
        if valor:
            params[campo] = valor

    response = requests.get(
        f"{API_BASE_URL}/api/veiculos/",
        headers=headers,
        params=params
    )

    if response.status_code != 200:
        return redirect("login")

    return render(
        request,
        "veiculos.html",
        {"veiculos": response.json(), "filtros": params}
    )

def veiculo_detalhe_view(request, id):
    token = request.session.get("access_token")
    if not token:
        return redirect("login")

    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(
        f"{API_BASE_URL}/api/veiculos/{id}/",
        headers=headers
    )

    if response.status_code != 200:
        return redirect("veiculos")

    return render(
        request,
        "veiculo_detalhe.html",
        {"veiculo": response.json()}
    )

def veiculo_novo_view(request):
    token = request.session.get("access_token")
    if not token:
        return redirect("login")

    if request.method == "POST":
        headers = {"Authorization": f"Bearer {token}"}

        response = requests.post(
            f"{API_BASE_URL}/api/veiculos/",
            headers=headers,
            json=request.POST.dict()
        )

        if response.status_code == 201:
            return redirect("veiculos")

    return render(request, "veiculo_form.html")

def veiculo_editar_view(request, id):
    token = request.session.get("access_token")
    if not token:
        return redirect("login")

    headers = {"Authorization": f"Bearer {token}"}

    if request.method == "POST":
        response = requests.put(
            f"{API_BASE_URL}/api/veiculos/{id}/",
            headers=headers,
            json=request.POST.dict()
        )
        return redirect("veiculos")

    response = requests.get(
        f"{API_BASE_URL}/api/veiculos/{id}/",
        headers=headers
    )

    return render(
        request,
        "veiculo_form.html",
        {"veiculo": response.json()}
    )

def veiculo_excluir_view(request, id):
    token = request.session.get("access_token")
    if not token:
        return redirect("login")

    headers = {"Authorization": f"Bearer {token}"}
    requests.delete(
        f"{API_BASE_URL}/api/veiculos/{id}/",
        headers=headers
    )

    return redirect("veiculos")

def logout_view(request):
    request.session.flush()
    return redirect("login")