import pytest
from order.models import Order
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_create_order():
    user = User.objects.create(username="daniel")
    order = Order.objects.create(user=user)

    assert order.user == user