from utils import clear_screen, pause, show_status, increase_hope

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