from game.heart_gem import increase_hope, increase_despair
from game.inventory import add_item
from game.ui import choose, pause, show_status, title


def level1(game):
    game.current_level = 1
    title("LEVEL 1 — THE AWAKENING")
    print("""
Cold stone presses against Elara's back.
Blood stains her sleeve, but she cannot remember the wound.
A dull Heart Gem is embedded in her palm.

A pale creature steps from the darkness.

"You came back."

It offers a hand.

"I can grant you one wish. A way out."
""".strip())

    pause()

    print("\nBefore answering, Elara searches the room.")
    add_item(game, "Old Key")
    add_item(game, "Torn Letter")
    add_item(game, "Carved Symbol")

    choice = choose(
        "What will Elara do?",
        ["Accept the wish", "Refuse the wish", "Demand the truth"],
    )

    if choice == 1:
        game.record_choice("accepted_wish")
        game.flags["envoy_trusted"] = True
        increase_despair(game, 15)
        print("\nThe Envoy smiles. The lock on the iron door clicks open.")
        print("But the Heart Gem feels colder than before.")
    elif choice == 2:
        game.record_choice("refused_wish")
        increase_hope(game, 10)
        print("\nThe Envoy's smile disappears.")
        print("A hidden passage opens behind the old bookshelf.")
    else:
        game.record_choice("demanded_truth")
        increase_hope(game, 5)
        print("\nElara raises the gem.")
        print("\"Tell me what you know.\"")
        print("The Envoy whispers: \"You have asked this before.\"")
        game.flags["dungeon_knows_elara"] = True

    show_status(game)
    if 1 not in game.completed_levels:
        game.completed_levels.append(1)
    game.current_level = 2
    pause("Press Enter to descend to Level 2...")
