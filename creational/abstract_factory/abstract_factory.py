from abc import ABC, abstractmethod


class AbstractProduct1(ABC):
    """Abstract Class for Product 1
        This is optional for Abstract Factory pattern
        but it represents other important OOP principle
        'Coding to interfaces and implementation'"""
    @abstractmethod
    def product_1_capability(self):
        pass


class AbstractProduct2(ABC):
    """Abstract Class for Product 2
        This is optional for Abstract Factory pattern
        but it represents other important OOP principle
        'Coding to interfaces and implementation'"""
    @abstractmethod
    def product_2_capability(self):
        pass


class AbstractFactory(ABC):
    """Abstract Factory is an abstract class that declares
       abstract create functions that create different Class' objects or interface
       It creates different product(s) of same family.
       In this case, it's product_1 and product_2"""

    @abstractmethod
    def create_product_1(self) -> AbstractProduct1:
        pass

    @abstractmethod
    def create_product_2(self) -> AbstractProduct2:
        pass


class Product1(AbstractProduct1):
    def product_1_capability(self):
        print('Product 1')


class Product2(AbstractProduct2):
    def product_2_capability(self):
        print('Product 2')


class ConcreteFactory(AbstractFactory):
    """This is important and does an implementation of
        AbstractFactory define earlier"""

    def create_product_1(self) -> Product1:
        return Product1()

    def create_product_2(self) -> Product2:
        return Product2()
