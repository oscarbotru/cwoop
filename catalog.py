class Product:
    id: int
    title: str
    price: float
    count: int
    category: int

    def __init__(self, *args, **kwargs):
        pass

    def __bool__(self):
        """
        Проверяет есть ли товар в наличии
        """
        pass

    def __len__(self):
        """
        Возвращает количество товара на складе
        """
        pass


class Category:
    id: int
    title: str
    description: str
    products: list

    def __init__(self):
        pass

    def __bool__(self):
        """
        Проверяет есть ли товар в категории
        """
        pass

    def __len__(self):
        """
        Возвращает количество наименований товаров, у которых есть наличие на складе
        """
        pass
