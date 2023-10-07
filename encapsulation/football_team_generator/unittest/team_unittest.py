from project.team import Team
from project.player import Player
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team("Team1", 99)
        self.player = Player("Bot1", 99, 99, 99, 99)
        
    def test_team_correct_initialization(self):
        self.assertEqual("Team1", self.team._Team__name)
        self.assertEqual(99, self.team._Team__rating)
        self.assertEqual([], self.team._Team__players)
        
    def test_add_player_method_returns_correct(self):
        result = self.team.add_player(self.player)
        
        self.assertIn(self.player, self.team._Team__players)
        
        self.assertEqual("Player Bot1 joined team Team1", result)
        
        # player already in test
        result = self.team.add_player(self.player)
        
        self.assertEqual("Player Bot1 has already joined", result)
        
    def test_remove_player_method_exisitng_player(self):
        self.team.add_player(self.player)
        
        removed_player = self.team.remove_player(self.player.name)
        
        self.assertEqual(self.player, removed_player)
        self.assertEqual(self.player.name, removed_player.name)
        self.assertNotIn(self.player, self.team._Team__players)
        
    def test_remove_player_method_non_exisitng_player(self):
        result = self.team.remove_player(self.player.name)
        
        self.assertEqual("Player Bot1 not found", result)
        
    def test_remove_player_method_player_not_in_list(self):
        result = self.team.remove_player(self.player.name)
        
        self.assertEqual("Player Bot1 not found", result)


if __name__ == "__main__":
    main()