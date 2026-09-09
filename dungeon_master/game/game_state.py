import json
from pathlib import Path


class GameState:
    def __init__(self):
        self.current_level = 1
        self.heart_gem = 60
        self.inventory = []
        self.choices = {}
        self.flags = {}
        self.completed_levels = []
        self.discovered_endings = []

    def add_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)

    def has_item(self, item):
        return item in self.inventory

    def change_heart(self, amount):
        self.heart_gem = max(0, min(100, self.heart_gem + amount))

    def record_choice(self, name, value=True):
        self.choices[name] = value

    def save(self, filename="savegame.json"):
        data = {
            "current_level": self.current_level,
            "heart_gem": self.heart_gem,
            "inventory": self.inventory,
            "choices": self.choices,
            "flags": self.flags,
            "completed_levels": self.completed_levels,
            "discovered_endings": self.discovered_endings,
        }
        Path(filename).write_text(json.dumps(data, indent=4), encoding="utf-8")

    @classmethod
    def load(cls, filename="savegame.json"):
        path = Path(filename)
        if not path.exists():
            return None

        data = json.loads(path.read_text(encoding="utf-8"))
        game = cls()
        game.current_level = data.get("current_level", 1)
        game.heart_gem = data.get("heart_gem", 60)
        game.inventory = data.get("inventory", [])
        game.choices = data.get("choices", {})
        game.flags = data.get("flags", {})
        game.completed_levels = data.get("completed_levels", [])
        game.discovered_endings = data.get("discovered_endings", [])
        return game
