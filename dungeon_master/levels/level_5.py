def level5(game):
    """Run Level 5 - The Heart of the Dungeon."""

    game.current_level = 5

    show_intro()
    reveal_truth(game)
    show_status(game)

    choice = get_final_choice()
    save_final_choice(game, choice)
    determine_ending(game, choice)

    # Mark Level 5 as completed
    if hasattr(game, "completed_levels"):
        if 5 not in game.completed_levels:
            game.completed_levels.append(5)


def show_intro():
    """Display the opening scene of Level 5."""

    print("\n" + "=" * 55)
    print("          LEVEL 5 - THE HEART OF THE DUNGEON")
    print("=" * 55)

    print("""
Elara steps through the final doorway.

The dungeon is completely silent.

No screams.
No chains.
No whispers.

At the centre of the chamber, something enormous
beats beneath the stone.

Her Heart Gem begins to glow.

A familiar voice comes from the darkness.

Envoy:
"You finally made it back, Elara."
""")

    input("Press Enter to continue...")


def reveal_truth(game):
    """Reveal Elara's connection to the dungeon."""

    print("\n" + "-" * 55)
    print("                     THE TRUTH")
    print("-" * 55)

    print("""
Elara walks towards the Heart.

The Heart Gem pulses in her hand.

Suddenly, memories begin to return.

She sees the girls who came before her.
She sees their wishes, their hope and their fear.

Then she sees herself.

Elara was never simply a prisoner.

She has stood before the Heart before.

She was here when the cycle began.

That is why the dungeon remembers her.
""")

    # Check whether an earlier level stored this memory.
    if hasattr(game, "flags"):
        if game.flags.get("dungeon_knows_elara"):
            print("""
A memory from the first chamber returns.

The Envoy had told her:

"You have asked this before."

Elara finally understands what those words meant.
""")

    input("Press Enter to continue...")


def show_status(game):
    """Show the Heart Gem if the shared game has one."""

    if hasattr(game, "heart_gem"):
        print("\n" + "-" * 55)
        print(f"Heart Gem: {game.heart_gem}/100")
        print("-" * 55)


def get_final_choice():
    """Ask the player for Elara's final decision."""

    print("\n" + "=" * 55)
    print("                    FINAL CHOICE")
    print("=" * 55)

    print("""
Everything that happened in the dungeon has led
Elara to this moment.

What will she do?

1. Escape the dungeon
2. Destroy the Heart
3. Take control of the Heart
""")

    while True:
        choice = input("Choose 1, 2, or 3: ").strip()

        if choice in ["1", "2", "3"]:
            return choice

        print("Invalid choice. Please enter 1, 2, or 3.")


def save_final_choice(game, choice):
    """Store the final decision in the shared game state."""

    choice_names = {
        "1": "escaped_dungeon",
        "2": "sacrificed_self",
        "3": "rewrote_law"
    }

    final_choice = choice_names[choice]

    # Use the team's record_choice method if it exists.
    if hasattr(game, "record_choice"):
        game.record_choice(final_choice)

    # Otherwise store it directly if choices exists.
    elif hasattr(game, "choices"):
        game.choices[final_choice] = True


def determine_ending(game, choice):
    """Choose an ending using the Heart Gem and final decision."""

    heart_gem = getattr(game, "heart_gem", 50)

    if heart_gem <= 0:
        loop_ending()

    elif choice == "1":
        runaway_ending()

    elif choice == "2":
        unmaking_ending()

    elif choice == "3":
        new_law_ending()


def runaway_ending():
    print("\n" + "=" * 55)
    print("               ENDING - THE RUNAWAY")
    print("=" * 55)

    print("""
Elara turns away from the Heart.

She runs through the chambers,
past the empty cells
and towards the final door.

For the first time, she feels cold night air.

She is free.

But deep beneath the earth...

the Heart continues to beat.

The dungeon waits.
""")


def unmaking_ending():
    print("\n" + "=" * 55)
    print("              ENDING - THE UNMAKING")
    print("=" * 55)

    print("""
Elara places both hands against the Heart.

She knows what destroying it may cost her.

But her final wish is not for herself.

It is for everyone trapped inside.

The Heart begins to crack.

The walls shake.
The chains break.

The cycle is finally broken.
""")


def new_law_ending():
    print("\n" + "=" * 55)
    print("               ENDING - THE NEW LAW")
    print("=" * 55)

    print("""
Elara reaches towards the Heart.

She does not destroy it.

Instead, she takes control of its power.

The dungeon bends to her will.

No girl will ever feed it with despair again.

Elara remains behind...

not as its prisoner,

but as its new guardian.
""")


def loop_ending():
    print("\n" + "=" * 55)
    print("                 ENDING - THE LOOP")
    print("=" * 55)

    print("""
The final light inside Elara's Heart Gem disappears.

Everything goes dark.

The dungeon whispers her name.

Her memories begin to fade.

...

Elara wakes on cold stone.

There is blood on her sleeve.

She does not remember whose it is.

A voice whispers from the darkness:

"You came back."
""")