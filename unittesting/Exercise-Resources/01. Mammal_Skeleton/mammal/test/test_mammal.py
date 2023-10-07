from project.mammal import Mammal

from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self) -> object:
        self.mammal =  Mammal("mammal1", "mammal_type1", "mammal_sound1")
        
    def test_mammal_initialized_correctly(self):
        self.assertEqual("mammal1", self.mammal.name)
        self.assertEqual("mammal_type1", self.mammal.type)
        self.assertEqual("mammal_sound1", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)
        
    def test_mammal_makes_sound_correctly(self):
        self.assertEqual("mammal1 makes mammal_sound1", self.mammal.make_sound())
        
    def test_mammal_get_kingdom_method(self):
        self.assertEqual("animals", self.mammal.get_kingdom())
        
    def test_mammal_info_method(self):
        self.assertEqual("mammal1 is of type mammal_type1", self.mammal.info())


if __name__ == "__main__":
    main()