from abc import ABC, abstractmethod, abstractproperty


class AbstractHouseBuilder(ABC):
    """
    Abstract Class "HouseBuilder" declares methods to create
    Room(s), 1 hall and 1 kitchen of the house object
    """

    @abstractproperty
    def house(self) -> None:
        pass

    @abstractmethod
    def start_building_new_house(self) -> None:
        pass

    @abstractmethod
    def build_room(self) -> None:
        pass

    @abstractmethod
    def build_hall(self) -> None:
        pass

    @abstractmethod
    def build_kitchen(self) -> None:
        pass


class House():
    """
    Different House implementations can have different interfaces.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(self.parts)
        print("House includes: {', '.join(self.parts)}")


class HouseBuilder(AbstractHouseBuilder):
    """
    ConcreteHouseBuilder defines all the methods in the HouseBuilder
    to give real implementation to it.
    Also this builder adds 3 rooms the houses it creates
    """
    _house = None

    def __init__(self) -> None:
        self.start_building_new_house()

    @property
    def house(self):
        return self._house

    def start_building_new_house(self) -> None:
        self._house = House()

    def build_room(self, seq=1) -> None:
        self._house.add(('Room' + str(seq)))

    def build_hall(self) -> None:
        self._house.add('hall')

    def build_kitchen(self) -> None:
        self._house.add('kitchen')


class Director:
    """
    Director is responsible for invoking the methods of builder in right order.
    """

    def __init__(self, builder: HouseBuilder) -> None:
        self._house_builder = builder

    @property
    def builder(self) -> HouseBuilder:
        return self._house_builder

    def build_1_bhk_house(self) -> None:
        self.builder.build_room(1)
        self.builder.build_hall()
        self.builder.build_kitchen()

    def build_2_bhk_house(self) -> None:
        for i in range(2):
            self.builder.build_room(i+1)
        self.builder.build_hall()
        self.builder.build_kitchen()

    def build_k_bhk_house(self, k) -> None:
        for i in range(k):
            self.builder.build_room(i+1)
        self.builder.build_hall()
        self.builder.build_kitchen()
