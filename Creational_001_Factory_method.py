'''
На основе
Абстрактно
https://refactoring.guru/ru/design-patterns/factory-method
или конкретно Python
https://github.com/ivgnk/design-patterns-python/blob/main/src/FactoryMethod/Conceptual/main.py

RU: Паттерн Фабричный Метод
Назначение: Определяет общий интерфейс для создания объектов в суперклассе,
позволяя подклассам изменять тип создаваемых объектов.

Также хорошо описано
https://webdevblog.ru/shablon-fabrichnogo-metoda-i-ego-realizaciya-v-python/
'''


# from __future__ import annotations
from abc import ABC, abstractmethod

class Product(ABC):
    """
    EN: The Product interface declares the operations that all concrete products
    must implement.

    RU: Интерфейс Продукта объявляет операции, которые должны выполнять все
    конкретные продукты.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
EN: Concrete Products provide various implementations of the Product interface.

RU: Конкретные Продукты предоставляют различные реализации интерфейса Продукта.
"""


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "Result of the ConcreteProduct1"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "Result of the ConcreteProduct2"


class Creator(ABC):
    """
    EN: The Creator class declares the factory method that is supposed to return
    an object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.

    RU: Класс Создатель объявляет фабричный метод, который должен возвращать
    объект класса Продукт. Подклассы Создателя обычно предоставляют реализацию
    этого метода.
    """

    @abstractmethod
    def factory_method(self):
        """
        EN: Note that the Creator may also provide some default implementation
        of the factory method.

        RU: Обратите внимание, что Создатель может также обеспечить реализацию
        фабричного метода по умолчанию.
        """
        pass

    def some_operation(self) -> str:
        """
        EN: Also note that, despite its name, the Creator's primary
        responsibility is not creating products. Usually, it contains some core
        business logic that relies on Product objects, returned by the factory
        method. Subclasses can indirectly change that business logic by
        overriding the factory method and returning a different type of product
        from it.

        RU: Также заметьте, что, несмотря на название, основная обязанность
        Создателя не заключается в создании продуктов. Обычно он содержит
        некоторую базовую бизнес-логику, которая основана на объектах Продуктов,
        возвращаемых фабричным методом. Подклассы могут косвенно изменять эту
        бизнес-логику, переопределяя фабричный метод и возвращая из него другой
        тип продукта.
        """

        # EN: Call the factory method to create a Product object.
        #
        # RU: Вызываем фабричный метод, чтобы получить объект-продукт.
        product = self.factory_method()

        # EN: Now, use the product.
        #
        # RU: Далее, работаем с этим продуктом.
        result = f"Creator: Тот же код Creator только что работал с {product.operation()}"

        return result


"""
RU: Конкретные Создатели переопределяют фабричный метод для того, чтобы изменить
тип результирующего продукта.
"""
class ConcreteCreator1(Creator):
    """
    RU: Обратите внимание, что сигнатура метода по-прежнему использует тип
    абстрактного продукта, хотя фактически из метода возвращается конкретный
    продукт. Таким образом, Создатель может оставаться независимым от конкретных
    классов продуктов.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


def client_code(creator: Creator) -> None:
    """
    RU: Клиентский код работает с экземпляром конкретного создателя, хотя и
    через его базовый интерфейс. Пока клиент продолжает работать с создателем
    через базовый интерфейс, вы можете передать ему любой подкласс создателя.
    """

    print(f"Client: Я не знаю класса создателя, но он все еще работает.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Запущено  ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Запущено  ConcreteCreator2.")
    client_code(ConcreteCreator2())