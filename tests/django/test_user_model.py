import pytest


@pytest.mark.django_db
def test_user_creation(user_factory):
    user = user_factory()
    assert user.username
    assert user.email
    assert user.first_name
    assert user.last_name
    assert user.is_staff is False
    assert user.is_active is True
    assert user.is_superuser is False
