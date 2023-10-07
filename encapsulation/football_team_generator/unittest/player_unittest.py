from project.player import Player
from unittest import TestCase, main


class TestPlayer(TestCase):
    def setUp(self) -> None:
        self.player = Player("Bot1", 99, 99, 99, 99)
        
    def test_player_correct_initialization(self):
        self.assertEqual("Bot1", self.player.name)
        
        # name mangling
        self.assertEqual("Bot1", self.player._Player__name)
        self.assertEqual(99, self.player._Player__sprint)
        self.assertEqual(99, self.player._Player__dribble)
        self.assertEqual(99, self.player._Player__passing)
        self.assertEqual(99, self.player._Player__shooting)
        
    def test__str__method_returns_correct(self):
        self.assertEqual("Player: Bot1\nSprint: 99\nDribble: 99\nPassing: 99\nShooting: 99", str(self.player))


if __name__ == "__main__":
    main()