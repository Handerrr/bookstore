import pytest
from order.serializers.order_serializer import OrderSerializer
from order.factories import OrderFactory
from product.factories import ProductFactory
@pytest.mark.django_db
def test_order_serializer_total():
    product1 = ProductFactory(price=40)
    product2 = ProductFactory(price=60)

    order = OrderFactory(product=[product1, product2])

    serializer = OrderSerializer(order)
    data = serializer.data

    assert data["total"] == 100

    @pytest.mark.django_db
    def test_order_serializer_products():
        product = ProductFactory(price=25)
        order = OrderFactory(product=[product])

        serializer = OrderSerializer(order)

        assert len(serializer.data["product"]) == 1