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


class Shop:
    """
    Класс для работы с магазином
    """
    products: list
    categories: list

    def __init__(self, *args, **kwargs):
        pass

    def get_categories(self):
        """
        Показать все категории пользователю в произвольном виде, главное, чтобы пользователь
        мог видеть идентификаторы (id) каждой категории
        """
        pass

    def get_products(self):
        """
        Запросить номер категории и вывести все товары, которые относятся к этой категории
        Обработать вариант отсутствия введенного номера
        """
        pass

    def get_product(self):
        """
        Запросить ввод номера товара и вывести всю информацию по нему в произвольном виде
        Обработать вариант отсутствия введенного номера
        """
        pass
