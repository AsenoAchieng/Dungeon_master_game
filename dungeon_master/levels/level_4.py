from ..ui import clear_screen, pause, show_status
from ..game_state import increase_hope

def play_level_4(game):
    clear_screen()
    print("==================================================")
    print("          LEVEL 4 - THE RITUAL CHAMBER            ")
    print("==================================================")
    print()
    print("The walls pulse like a living heart.")
    print("Chains disappear into the floor.")
    print("A vast ritual circle surrounds a black crystal.")
    print()
    print("The truth becomes clear: the dungeon feeds on despair.")
    print()
    print("Mira arrives and holds back a shadow long enough for Elara to pass.")

    increase_hope(game, 10)

    if "envoy_confessed" in game.flags:
        print("The Envoy waits beside the ritual circle.")

    if game.is_corrupted(game):
        print("The Heart Gem is black. Elara's hands begin to change.")

        print()
    print("The ritual can be broken in one of three ways:")
    print("1. Break the crystal")
    print("2. Protect the Heart Gem")
    print("3. Ask the Envoy for the final truth")
    print()

    choice = input("> ")

    if choice == "1":
        game.record_choice("broke_crystal")
        increase_hope(game, 5)
        print("Elara strikes the crystal. The dungeon begins to shake...")
        game.completed_levels.append(4)
        game.current_level = 5
        pause("Press Enter to face the Heart of the Dungeon...")

    elif choice == "2":
        game.record_choice("protected_gem")
        increase_hope(game, 10)
        print("Mira shields the gem. For the first time, it shines clearly.")
        game.completed_levels.append(4)
        game.current_level = 5
        pause("Press Enter to face the Heart of the Dungeon...")

    elif choice == "3":
        game.record_choice("confronted_envoy")
        print("The Envoy finally speaks plainly.")
        print("\"I did not create the cycle... only kept it alive.\"")
        game.flags["envoy_confessed"] = True

        show_status(game)

    if 4 not in game.completed_levels:
        game.completed_levels.append(4)
        game.current_level = 5

    pause("Press Enter to enter the Heart of the Dungeon...")