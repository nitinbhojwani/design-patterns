import unittest
from .house_builder import HouseBuilder
from .house_builder import Director


class TestHouseBuilder(unittest.TestCase):
    """
    Replicate Client's behavior of creating HouseBuilder object,
    passing that to Director object and asking it to create
    different types of houses for us
    """

    def setUp(self):
        self.builder = HouseBuilder()
        self.director = Director(self.builder)

    def test_create_1_bhk_house(self):
        self.director.build_1_bhk_house()
        parts = ['Room1', 'hall', 'kitchen']
        assert self.director.builder.house.parts == parts
        # self.director.builder.house.list_parts()

    def test_create_2_bhk_house(self):
        self.director.build_2_bhk_house()
        parts = ['Room1', 'Room2', 'hall', 'kitchen']
        assert self.director.builder.house.parts == parts
        # self.director.builder.house.list_parts()

    def test_create_k_bhk_house(self):
        k = 5
        self.director.build_k_bhk_house(k)
        parts = ['Room1', 'Room2', 'Room3',
                 'Room4', 'Room5', 'hall', 'kitchen']
        self.director.builder.house.parts == parts
        # self.director.builder.house.list_parts()

    def tearDown(self):
        del self.director
        del self.builder
