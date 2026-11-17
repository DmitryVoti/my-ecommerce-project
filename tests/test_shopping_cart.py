import pytest
from src.product import Product
from src.shopping_cart import ShoppingCart

@pytest.fixture
def sample_product():
    return Product("prod_1", "Смартфон", 500.0, 10)

def test_add_product_success(sample_product):
    cart = ShoppingCart()
    cart.add_product(sample_product, 2)
    assert cart.calculate_total() == 1000.0

def test_add_zero_quantity_raises(sample_product):
    cart = ShoppingCart()
    with pytest.raises(ValueError, match="Количество должно быть положительным"):
        cart.add_product(sample_product, 0)

def test_add_negative_quantity_raises(sample_product):
    cart = ShoppingCart()
    with pytest.raises(ValueError, match="Количество должно быть положительным"):
        cart.add_product(sample_product, -1)

def test_add_more_than_stock_raises(sample_product):
    cart = ShoppingCart()
    with pytest.raises(ValueError, match="Недостаточно товара на складе"):
        cart.add_product(sample_product, 11)

def test_add_existing_product_increases_quantity(sample_product):
    cart = ShoppingCart()
    cart.add_product(sample_product, 2)
    cart.add_product(sample_product, 3)
    assert cart.calculate_total() == 500.0 * 5

def test_add_existing_product_exceeds_stock_raises(sample_product):
    cart = ShoppingCart()
    cart.add_product(sample_product, 8)
    with pytest.raises(ValueError, match="Недостаточно товара на складе"):
        cart.add_product(sample_product, 3)

def test_remove_product_completely(sample_product):
    cart = ShoppingCart()
    cart.add_product(sample_product, 2)
    cart.remove_product("prod_1")
    assert cart.calculate_total() == 0.0

def test_remove_product_partially(sample_product):
    cart = ShoppingCart()
    cart.add_product(sample_product, 5)
    cart.remove_product("prod_1", 3)
    assert cart.calculate_total() == 500.0 * 2

def test_remove_product_all_via_quantity(sample_product):
    cart = ShoppingCart()
    cart.add_product(sample_product, 5)
    cart.remove_product("prod_1", 5)
    assert cart.calculate_total() == 0.0

def test_remove_nonexistent_product_raises(sample_product):
    cart = ShoppingCart()
    with pytest.raises(KeyError, match="Товар отсутствует в корзине"):
        cart.remove_product("prod_999")

def test_remove_negative_quantity_raises(sample_product):
    cart = ShoppingCart()
    cart.add_product(sample_product, 5)
    with pytest.raises(ValueError, match="Количество для удаления должно быть положительным"):
        cart.remove_product("prod_1", -1)