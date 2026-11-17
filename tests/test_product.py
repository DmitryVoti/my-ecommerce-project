import pytest
from src.product import Product

def test_product_creation_success():
    p = Product("prod_1", "Телефон", 1000.0, 5)
    assert p.id == "prod_1"
    assert p.name == "Телефон"
    assert p.price == 1000.0
    assert p.stock == 5

def test_product_negative_price_raises():
    with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
        Product("prod_1", "Телефон", -100.0, 5)

def test_product_negative_stock_raises():
    with pytest.raises(ValueError, match="Количество на складе не может быть отрицательным"):
        Product("prod_1", "Телефон", 1000.0, -1)