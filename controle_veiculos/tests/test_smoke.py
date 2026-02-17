import pytest

@pytest.mark.django_db
def test_django_is_up():
    assert True