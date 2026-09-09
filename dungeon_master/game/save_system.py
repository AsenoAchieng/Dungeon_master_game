from pathlib import Path

SAVE_FILE = "savegame.json"


def save_game(game):
    game.save(SAVE_FILE)
    print("\nGame saved successfully.")


def load_game():
    return __import__("game.game_state", fromlist=["GameState"]).GameState.load(SAVE_FILE)


def save_exists():
    return Path(SAVE_FILE).exists()
