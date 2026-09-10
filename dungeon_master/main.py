from dungeon_master.game.endings import ending_tracker
from dungeon_master.game.game_state import GameState
from dungeon_master.game.inventory import show_inventory
from dungeon_master.game.save_system import load_game, save_game, save_exists
from dungeon_master.game.ui import choose, clear, pause, show_status, title
from dungeon_master.levels.level_1 import level1
from dungeon_master.levels.level_2 import level2
from dungeon_master.levels.level_4 import level4

GAME_NAME = "DUNGEON MASTER"


def banner():
    print("=" * 62)
    print(GAME_NAME.center(62))
    print("Every choice leaves a mark.".center(62))
    print("=" * 62)


def main_menu():
    while True:
        clear()
        banner()
        print("\nA dark, choice-driven dungeon-escape adventure.\n")

        options = ["New Game", "Continue", "Ending Tracker", "Settings", "Exit"]
        choice = choose("Main Menu", options)

        if choice == 1:
            clear()
            game = GameState()
            play_game(game)
            
        elif choice == 2:
            game = load_game()
            if game is None:
                print("\nNo save game was found.")
                pause()
            else:
                clear()
                print("Save loaded successfully.")
                pause()
                play_game(game)
        elif choice == 3:
            clear()
            game = load_game() or GameState()
            ending_tracker(game)
        elif choice == 4:
            settings()
        else:
            print("\nThe dungeon waits for your return...")
            break


def play_game(game):
    levels = {
        1: level1,
         2: level2,  # not built yet
        # 3: level3,  # not built yet
        4: level4,  
        # 5: level5,  # not built yet
    }

    while game.current_level <= 5:
        current = game.current_level

        if current not in levels:
            print(f"\nLevel {current} isn't built yet. Stopping here for now.")
            break

        level_function = levels[current]
        level_function(game)

        # Save after each completed level.
        save_game(game)

        if current == 5:
            break

        next_level = game.current_level
        if next_level not in levels:
            break

    print("\nRun complete.")
    show_status(game)
    pause("Press Enter to return to the main menu...")


def settings():
    clear()
    title("SETTINGS")
    print("\nCurrent version uses simple terminal output.")
    print("Text speed: Instant")
    print("Audio: Not included in CLI version")
    print("Accessibility: Numbered choices + readable text")
    pause()


if __name__ == "__main__":
    main_menu()
from levels.level_2 import level2



GAME_NAME = "DUNGEON MASTER"

 
def banner():
    print("=" * 62)
    print(GAME_NAME.center(62))
    print("Every choice leaves a mark.".center(62))
    print("=" * 62)


def main_menu():
    while True:
        clear()
        banner()
        print("\nA dark, choice-driven dungeon-escape adventure.\n")

        options = ["New Game", "Continue", "Ending Tracker", "Settings", "Exit"]
        choice = choose("Main Menu", options)

        if choice == 1:
            clear()
            game = GameState()
            play_game(game)
        elif choice == 2:
            game = load_game()
            if game is None:
                print("\nNo save game was found.")
                pause()
            else:
                clear()
                print("Save loaded successfully.")
                pause()
                play_game(game)
        elif choice == 3:
            clear()
            game = load_game() or GameState()
            ending_tracker(game)
        elif choice == 4:
            settings()
        else:
            print("\nThe dungeon waits for your return...")
            break


def play_game(game):
    levels = {
        1: level1,
        # 2: level2,  # not built yet
        # 3: level3,  # not built yet
        # 4: level4,  # not built yet
        # 5: level5,  # not built yet
    }

    while game.current_level <= 5:
        current = game.current_level

        if current not in levels:
            print(f"\nLevel {current} isn't built yet. Stopping here for now.")
            break

        level_function = levels[current]
        level_function(game)

        # Save after each completed level.
        save_game(game)

        if current == 5:
            break

        next_level = game.current_level
        if next_level not in levels:
            break

    print("\nRun complete.")
    show_status(game)
    pause("Press Enter to return to the main menu...")


def settings():
    clear()
    title("SETTINGS")
    print("\nCurrent version uses simple terminal output.")
    print("Text speed: Instant")
    print("Audio: Not included in CLI version")
    print("Accessibility: Numbered choices + readable text")
    pause()


if __name__ == "__main__":
    main_menu()