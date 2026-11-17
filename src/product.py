class Product:
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if stock < 0:
            raise ValueError("Количество на складе не может быть отрицательным")

        self.id = product_id
        self.name = name
        self.price = price
        self.stock = stock