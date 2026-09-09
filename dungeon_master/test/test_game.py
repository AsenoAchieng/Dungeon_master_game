import unittest

from game.game_state import GameState
from game.endings import determine_ending


class TestDungeonMaster(unittest.TestCase):
    def test_heart_gem_stays_between_zero_and_one_hundred(self):
        game = GameState()
        game.change_heart(1000)
        self.assertEqual(game.heart_gem, 100)
        game.change_heart(-1000)
        self.assertEqual(game.heart_gem, 0)

    def test_inventory_does_not_duplicate(self):
        game = GameState()
        game.add_item("Old Key")
        game.add_item("Old Key")
        self.assertEqual(game.inventory, ["Old Key"])

    def test_loop_ending(self):
        game = GameState()
        game.heart_gem = 0
        self.assertEqual(determine_ending(game), "loop")

    def test_unmaking_ending(self):
        game = GameState()
        game.choices["sacrificed_self"] = True
        self.assertEqual(determine_ending(game), "unmaking")

    def test_new_law_ending(self):
        game = GameState()
        game.choices["rewrote_law"] = True
        self.assertEqual(determine_ending(game), "new_law")

    def test_default_runaway_ending(self):
        game = GameState()
        self.assertEqual(determine_ending(game), "runaway")


if __name__ == "__main__":
    unittest.main()
