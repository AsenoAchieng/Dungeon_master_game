from game.ui import slow_print, choose, title, pause

#code for lvl 3-forgotten library story arc
VALID_SEARCHES = ["escapees", "symbol", "own_name"]

def show_intro(state):
    title("LEVEL 3 — THE FORGOTTEN LIBRARY")

    slow_print("Shelves of rotting books rise into darkness overhead.")
    slow_print("Every spine is a name. Every book, it seems, is someone's ending.")

    if state.flags.get("ally") == "girl":
        slow_print('\nThe girl runs her fingers along the shelves. "I\'ve read some of these," she admits quietly.')

def search_shelves(state):
    choice = choose("Where do you look first?", [
        "Search for accounts of people who escaped",
        "Search for anything about the symbol on the wall",
        "Search for your own name",
    ]) - 1

    if choice == 0:
        searched = "escapees"
        slow_print("\nYou find three accounts of escape. All three end the same way:")
        slow_print('"...and she was never seen outside these walls again."')
        state.nudge(courage=-1, curiosity=1)
    elif choice == 1:
        searched = "symbol"
        slow_print("\nA thin volume describes the symbol as a 'binding mark' — used to seal something IN, not to keep people out.")
        state.set_flag("knows_binding", True)
        state.nudge(curiosity=2)
    else:
        searched = "own_name"
        slow_print("\nYour hand finds a book before you're even looking for it.")
        slow_print("The spine reads: ELARA.")
        state.nudge(curiosity=2, courage=1)

    if searched not in VALID_SEARCHES:
        print("search area must be escapees, symbol, or own_name")

    pause()

def find_own_book(state):
    slow_print("\nWhether you looked for it or not, the book with your name finds you eventually.")
    slow_print("You open it. The pages describe a girl waking on cold stone. Blood on her sleeve.")
    slow_print("A voice saying: \"You came back.\"")
    slow_print("\nIt describes exactly what you did five minutes ago.")

    reveal_choice = choose("What do you do with this?", [
        "Keep reading — find out how the story ends",
        "Slam the book shut and refuse to know",
    ]) - 1

    if reveal_choice == 0:
        slow_print("\nThe next blank page slowly fills with ink as you watch, writing itself in real time.")
        slow_print('The last line, written just now: "She always wants to know how it ends."')
        state.set_flag("found_own_book", True)
        state.set_flag("accepted_truth", True)
        state.nudge(curiosity=3, trust=1)
    else:
        slow_print("\nYou shut it hard. Somewhere below, something shudders, like a held breath released.")
        state.set_flag("found_own_book", True)
        state.nudge(courage=-1, trust=-1)

    pause()

def level3(state):
    show_intro(state)
    search_shelves(state)
    find_own_book(state)
    state.current_level = 4
    return state