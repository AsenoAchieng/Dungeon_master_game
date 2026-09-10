from game.ui import title, pause


ENDING_TEXT = {
    "runaway": (
        "THE RUNAWAY",
        "Elara reaches the surface. Behind her, the dungeon goes silent. "
        "She is free—but deep below, another locked door begins to open. "
        "The cycle has survived."
    ),
    "unmaking": (
        "THE UNMAKING",
        "Elara spends her final wish on everyone except herself. The dungeon "
        "collapses into light, releasing the trapped girls. Her name fades "
        "from every record, but her sacrifice breaks the cycle."
    ),
    "new_law": (
        "THE NEW LAW",
        "Elara takes the Heart of the Dungeon and changes its oldest rule: "
        "despair will no longer feed the prison. She becomes its guardian, "
        "waiting for the day nobody needs rescuing."
    ),
    "loop": (
        "THE LOOP",
        "The Heart Gem turns completely black. Elara's body becomes a shadow "
        "with a girl's voice trapped inside it. When she opens her eyes again, "
        "she is lying on cold stone. A pale creature whispers: 'You came back.'"
    ),
}


def determine_ending(game):
    if game.heart_gem <= 0:
        return "loop"
    if game.choices.get("sacrificed_self"):
        return "unmaking"
    if game.choices.get("rewrote_law"):
        return "new_law"
    return "runaway"


def show_ending(game):
    ending = determine_ending(game)
    title_text, story = ENDING_TEXT[ending]
    title(f"ENDING: {title_text}")
    print("\n" + story)
    if ending not in game.discovered_endings:
        game.discovered_endings.append(ending)
    pause()
    return ending


def ending_tracker(game):
    title("ENDING TRACKER")
    names = {
        "runaway": "The Runaway",
        "unmaking": "The Unmaking",
        "new_law": "The New Law",
        "loop": "The Loop",
    }
    for key in names:
        marker = "✓" if key in game.discovered_endings else "?"
        print(f"{marker} {names[key]}")
    pause()
