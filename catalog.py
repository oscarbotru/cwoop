from connector import Connector


class Product:
    id: int
    title: str
    price: float
    count: int
    category: int

    def __init__(self, data_json):
        self.id = data_json.get('id')
        self.title = data_json.get('title')
        self.price = data_json.get('price')
        self.count = data_json.get('count')
        self.category = data_json.get('category')

    def __str__(self):
        return f'Продукт "{self.title}" с количеством на складе {self.count} с ценой {self.price} за кг'

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
    # products: list
    # categories: list

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
        cat_number = input('Введите номер категории: ')

        while not cat_number.isdigit():
            cat_number = input('Введите НОМЕР категории, а не что-то другое: ')

        product_connector = Connector('products.json')
        products_list = product_connector.select({'category': int(cat_number)})
        for prod in products_list:
            prod_obj = Product(prod)
            print(prod_obj)

    def get_product(self):
        """
        Запросить ввод номера товара и вывести всю информацию по нему в произвольном виде
        Обработать вариант отсутствия введенного номера
        """
        pass


if __name__ == '__main__':
    my_shop = Shop()
    my_shop.get_products()
