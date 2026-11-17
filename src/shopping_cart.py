from src.product import Product

class ShoppingCart:
    def __init__(self):
        # Словарь: product_id -> {"product": Product, "quantity": int}
        self._items = {}

    def add_product(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")
        if quantity > product.stock:
            raise ValueError("Недостаточно товара на складе")

        if product.id in self._items:
            new_quantity = self._items[product.id]["quantity"] + quantity
            if new_quantity > product.stock:
                raise ValueError("Недостаточно товара на складе")
            self._items[product.id]["quantity"] = new_quantity
        else:
            self._items[product.id] = {"product": product, "quantity": quantity}

    def remove_product(self, product_id: str, quantity: int = None):
        if product_id not in self._items:
            raise KeyError("Товар отсутствует в корзине")

        if quantity is None:
            del self._items[product_id]
        else:
            if quantity <= 0:
                raise ValueError("Количество для удаления должно быть положительным")
            self._items[product_id]["quantity"] -= quantity
            if self._items[product_id]["quantity"] <= 0:
                del self._items[product_id]

    def calculate_total(self) -> float:
        total = 0.0
        for item in self._items.values():
            total += item["product"].price * item["quantity"]
        return total