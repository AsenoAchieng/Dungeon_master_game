from game.heart_gem import increase_hope, increase_despair
from game.ui import choose, pause, title


def level2(game):
    game.current_level = 2
    title("LEVEL 2 — THE PRISON")

    print("""
The corridor opens into a row of cells, doors hanging off rusted hinges.
In the last cell, something moves.
A girl, thin and pale, presses against the bars.
"Don't trust the dungeon," she hisses.
""".strip())

    if game.flag("examined_symbol"):
        print("\nShe flinches when she sees the mark still glowing faintly on your palm.")
        print('"You... you\'re one of them, aren\'t you."')

    choice = choose(
        "What do you do?",
        [
            "Rescue her — pick the lock with the old key",
            "Leave her — something feels wrong here",
            "Question her before deciding",
        ],
    )

    if choice == 1:
        print("\nThe key fits. The lock groans open.")
        print('"Thank you," she whispers. "I\'ll help you however I can."')
        game.set_flag("rescued_girl", True)
        game.flags["ally"] = "girl"
        increase_hope(game, 10)
    elif choice == 2:
        print("\nYou step back. Her eyes widen, but she doesn't beg.")
        print('"...Smart," she mutters, almost to herself.')
        game.set_flag("left_girl", True)
        increase_despair(game, 10)
    else:
        print("\nYou keep your distance and ask her what she knows.")
        _question_her(game)

    pause()

    print("\nDeeper in the prison block, you find a rusted lever and a second locked door.")
    lever_choice = choose(
        "A lever juts from the wall, half-broken. Do you pull it?",
        ["Pull the lever", "Leave it alone"],
    )
    if lever_choice == 1:
        print("\nGears grind somewhere below. A distant door unlocks — or does something else unlock too?")
        game.set_flag("pulled_lever", True)
        increase_hope(game, 5)
    else:
        print("\nYou leave the mechanism untouched. Some things should stay buried.")
        increase_hope(game, 3)

    pause()
    game.current_level = 3
    if 2 not in game.completed_levels:
        game.completed_levels.append(2)
    return game


def _question_her(game):
    print('\n"What is this place?" you ask.')
    print('She studies you for a long moment.')
    print('"It remembers everyone who\'s ever tried to leave. It remembers YOU."')

    follow_up = choose(
        '"What do you mean, remembers me?"',
        ["Press her for more", "Back away — you're not ready to hear this"],
    )
    if follow_up == 1:
        print('\n"You\'ve been here before," she says. "More than once. It always resets."')
        game.set_flag("questioned_girl", True)
        increase_hope(game, 5)
    else:
        print("\nYou turn away before she can say more. The words follow you anyway.")
        game.set_flag("questioned_girl", True)
        increase_despair(game, 3)