import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_get_veiculos_sem_auth_retorna_403(client):
    url = reverse("veiculos-list")
    response = client.get(url)
    assert response.status_code == 403

@pytest.mark.django_db
def test_get_veiculos_com_user_autenticado_retorna_200(client):
    user = User.objects.create_user(username="user", password="123")
    client.force_login(user)

    url = reverse("veiculos-list")
    response = client.get(url)

    assert response.status_code == 200