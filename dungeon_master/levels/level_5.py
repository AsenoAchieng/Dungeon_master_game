def level5(game):
    """Runs Level 5: The Heart of the Dungeon."""

    game.current_level = 5

    print("\nLevel 5: The Heart of the Dungeon")

    print("""
Elara enters the final chamber.

In the middle of the room is the Heart of the Dungeon.
Her Heart Gem begins to glow.

A voice whispers:

"You finally made it back, Elara."
""")

    reveal_truth(game)
    choice = final_choice()
    save_choice(game, choice)
    show_ending(game, choice)

    if 5 not in game.completed_levels:
        game.completed_levels.append(5)


def reveal_truth(game):
    """Reveals Elara's connection to the dungeon."""

    print("""
The Truth

Elara touches the Heart and her memories return.

She remembers the girls who were trapped here before her.
Then she remembers herself.

She has been here before.

Elara was never just another prisoner.

That is why the dungeon remembers her.
""")

    if game.flags.get("dungeon_knows_elara"):
        print("""
Elara remembers the Envoy's words:

"You have asked this before."

Now she finally understands.
""")


def final_choice():
    """Gets the player's final decision."""

    print("""
What will Elara do?

1. Escape the dungeon
2. Destroy the Heart
3. Take control of the Heart
""")

    while True:
        choice = input("Choose 1, 2 or 3: ")

        if choice in ["1", "2", "3"]:
            return choice

        print("Invalid choice. Try again.")


def save_choice(game, choice):
    """Saves the player's choice."""

    if choice == "1":
        game.record_choice("escaped_dungeon")

    elif choice == "2":
        game.record_choice("sacrificed_self")

    else:
        game.record_choice("rewrote_law")


def show_ending(game, choice):
    """Shows the ending based on the player's choices."""

    if game.heart_gem <= 0:
        print("""
THE LOOP

Everything goes dark.

Elara wakes on the cold stone again.

"You came back."

The dungeon has won.
""")

    elif choice == "1":
        print("""
THE RUNAWAY

Elara escapes into the night.

She is free, but deep underground
the Heart continues to beat.
""")

    elif choice == "2":
        print("""
THE UNMAKING

Elara destroys the Heart.

The dungeon begins to collapse
and the prisoners are freed.

The cycle is broken.
""")

    else:
        print("""
THE NEW LAW

Elara takes control of the Heart.

The dungeon bends to her will.

She remains behind,
not as its prisoner,
but as its new guardian.
""")