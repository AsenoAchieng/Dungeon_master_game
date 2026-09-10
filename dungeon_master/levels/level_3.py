#!/usr/bin/env python3

# level 3 of the game. made it a class since we're doing OOP now.
# tried out the property/setter thing from the coffee.py file in one of the labs.

from utils import slow_print, menu, banner, pause


class ForgottenLibrary:

    # only these 3 searches allowed.
    VALID_SEARCHES = ("escapees", "symbol", "own_name")

    def __init__(self, state):
        self.state = state
        self.searched = None   # haven't searched anything yet(empty)

    @property
    def searched(self):
        return self._searched

    # check it's a real search before saving, otherwise just warn
    @searched.setter
    def searched(self, area):
        if area is None or area in ForgottenLibrary.VALID_SEARCHES:
            self._searched = area
        else:
            print("search area must be escapees, symbol, or own_name")

    def show_intro(self):
        banner("LEVEL 3 — THE FORGOTTEN LIBRARY")

        slow_print("Shelves of rotting books rise into darkness overhead.")
        slow_print("Every spine is a name. Every book, it seems, is someone's ending.")

        # girl only says this if she's actually with you
        if self.state.flags.get("ally") == "girl":
            slow_print('\nThe girl runs her fingers along the shelves. "I\'ve read some of these," she admits quietly.')

    def search_shelves(self):
        # menu gives back the number they picked (0,1,2)
        choice = menu("Where do you look first?", [
            "Search for accounts of people who escaped",
            "Search for anything about the symbol on the wall",
            "Search for your own name",
        ])

        if choice == 0:
            self.searched = "escapees"
            slow_print("\nYou find three accounts of escape. All three end the same way:")
            slow_print('"...and she was never seen outside these walls again."')
            self.state.nudge(courage=-1, curiosity=1)
        elif choice == 1:
            self.searched = "symbol"
            slow_print("\nA thin volume describes the symbol as a 'binding mark' — used to seal something IN, not to keep people out.")
            self.state.set_flag("knows_binding", True)   # need this for later
            self.state.nudge(curiosity=2)
        else:
            self.searched = "own_name"
            slow_print("\nYour hand finds a book before you're even looking for it.")
            slow_print("The spine reads: ELARA.")
            self.state.nudge(curiosity=2, courage=1)

        pause()

    def find_own_book(self):
        # this part happens no matter what was picked before(Compulsory)
        slow_print("\nWhether you looked for it or not, the book with your name finds you eventually.")
        slow_print("You open it. The pages describe a girl waking on cold stone. Blood on her sleeve.")
        slow_print("A voice saying: \"You came back.\"")
        slow_print("\nIt describes exactly what you did five minutes ago.")

        reveal_choice = menu("What do you do with this?", [
            "Keep reading — find out how the story ends",
            "Slam the book shut and refuse to know",
        ])

        if reveal_choice == 0:
            slow_print("\nThe next blank page slowly fills with ink as you watch, writing itself in real time.")
            slow_print('The last line, written just now: "She always wants to know how it ends."')
            self.state.set_flag("found_own_book", True)
            self.state.set_flag("accepted_truth", True)
            self.state.nudge(curiosity=3, trust=1)
        else:
            slow_print("\nYou shut it hard. Somewhere below, something shudders, like a held breath released.")
            self.state.set_flag("found_own_book", True)   # they still found it, just didn't read it
            self.state.nudge(courage=-1, trust=-1)

        pause()

    def play(self):
        # just run the 3 parts in order
        self.show_intro()
        self.search_shelves()
        self.find_own_book()
        self.state.level = 4   # go to next level
        return self.state


# game still calls play(state) so leaving this here. makes the object and runs it
def play(state):
    level = ForgottenLibrary(state)
    return level.play()