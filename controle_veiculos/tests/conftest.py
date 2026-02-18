import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user_token():
    user = User.objects.create_user(username="user", password="123")
    token = AccessToken.for_user(user)
    return str(token)

@pytest.fixture
def admin_token():
    admin = User.objects.create_superuser(
        username="admin", password="123", email="admin@test.com"
    )
    token = AccessToken.for_user(admin)
    return str(token)