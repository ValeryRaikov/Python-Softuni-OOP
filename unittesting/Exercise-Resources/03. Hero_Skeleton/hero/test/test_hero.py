from project.hero import Hero

from unittest import TestCase, main


class TestHero(TestCase):
    def setUp(self) -> object:
        self.hero = Hero("Hero1", 1, 100, 75)
        self.enemy = Hero("Enemy1", 1, 100, 50)
        
    def test_hero_initialized_correctly(self):
        self.assertEqual("Hero1", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(75, self.hero.damage)
        
    def test_hero_battles_with_the_same_name_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
            
        self.assertEqual("You cannot fight yourself", str(ex.exception))
        
    def test_hero_battles_with_zero_or_negative_health_raises(self):
        self.hero.health = -1
        
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
            
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))
        
    def test_enemy_battles_with_zero_or_negative_health_raises(self):
        self.enemy.health = -1
        
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
            
        self.assertEqual("You cannot fight Enemy1. He needs to rest", str(ex.exception))
        
    def test_battle_removes_health_after_draw(self):
        self.hero.health = 50
        self.enemy.health = 60
        
        result = self.hero.battle(self.enemy)
        
        self.assertEqual(-15, self.enemy.health)
        self.assertEqual(0, self.hero.health)
        self.assertEqual("Draw", result)
        
    def test_battle_hero_wins_improved_stats_expected(self):
        self.enemy.health = 50
        
        result = self.hero.battle(self.enemy)
        
        self.assertEqual(2, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(80, self.hero.damage)
        self.assertEqual("You win", result)
        
    def test_battle_enemy_wins_improved_stats_expected(self):
        self.hero.health = 50
        
        result = self.hero.battle(self.enemy)
        
        self.assertEqual(2, self.enemy.level)
        self.assertEqual(30, self.enemy.health)
        self.assertEqual(55, self.enemy.damage)
        self.assertEqual("You lose", result)
        
    def test__repr_method_return_correct_message(self):
        self.assertEqual("Hero Hero1: 1 lvl\nHealth: 100\nDamage: 75\n", str(self.hero))


if __name__ == "__main__":
    main()