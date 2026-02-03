import pytest
from order.factories import OrderFactory
from product.factories import ProductFactory
@pytest.mark.django_db
def test_order_factory_with_products():
    p1 = ProductFactory(price=10)
    p2 = ProductFactory(price=30)

    order = OrderFactory(product=[p1, p2])

    assert order.product.count() == 2