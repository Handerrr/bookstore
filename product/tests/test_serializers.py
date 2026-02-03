import pytest
from product.serializers.product_serializer import ProductSerializer
from product.models.product import Product
from product.models.category import Category

@pytest.mark.django_db
def test_product_serializer_with_category():
    category = Category.objects.create(title="Eletrônicos", slug="eletronicos")

    product = Product.objects.create(
        title="Mouse",
        price=120
    )
    product.category.add(category)

    serializer = ProductSerializer(product)
    data = serializer.data

    assert data["title"] == "Mouse"
    assert len(data["category"]) == 1
    assert data["category"][0]["title"] == "Eletrônicos"