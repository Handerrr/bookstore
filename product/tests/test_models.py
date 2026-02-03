import pytest
from product.models.product import Product
from product.models.category import Category

@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(
        title="Camiseta",
        description="Camiseta preta",
        price=50,
        active=True
    )

    assert product.title == "Camiseta"
    assert product.price == 50

    @pytest.mark.django_db
    def test_product_with_categories():
        category1 = Category.objects.create(title="Roupas", slug="roupas")
        category2 = Category.objects.create(title="Promo", slug="promo")

        product = Product.objects.create(
            title="Tênis",
            price=200
        )

        product.category.add(category1, category2)

        assert product.category.count() == 2
        assert category1 in product.category.all()