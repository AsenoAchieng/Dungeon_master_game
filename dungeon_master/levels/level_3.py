#!/usr/bin/env python3

# level 3 of the game. made it a class since we're doing OOP now.
# tried out the property/setter thing from the coffee.py file in one of the labs.

from dungeon_master.game.heart_gem import increase_hope, increase_despair
from dungeon_master.game.ui import choose, pause, title


class ForgottenLibrary:

    # only these 3 searches allowed.
    VALID_SEARCHES = ("escapees", "symbol", "own_name")

    def __init__(self, game):
        self.game = game
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
        title("LEVEL 3 — THE FORGOTTEN LIBRARY")

        print("Shelves of rotting books rise into darkness overhead.")
        print("Every spine is a name. Every book, it seems, is someone's ending.")

        # girl only says this if she's actually with you
        if self.game.flags.get("ally") == "girl":
            print('\nThe girl runs her fingers along the shelves. "I\'ve read some of these," she admits quietly.')

    def search_shelves(self):
        choice = choose("Where do you look first?", [
            "Search for accounts of people who escaped",
            "Search for anything about the symbol on the wall",
            "Search for your own name",
        ])

        if choice == 1:
            self.searched = "escapees"
            print("\nYou find three accounts of escape. All three end the same way:")
            print('"...and she was never seen outside these walls again."')
            increase_despair(self.game, 5)
        elif choice == 2:
            self.searched = "symbol"
            print("\nA thin volume describes the symbol as a 'binding mark' — used to seal something IN, not to keep people out.")
            self.game.set_flag("knows_binding", True)   # need this for later
            increase_hope(self.game, 5)
        else:
            self.searched = "own_name"
            print("\nYour hand finds a book before you're even looking for it.")
            print("The spine reads: ELARA.")
            increase_hope(self.game, 8)

        pause()

    def find_own_book(self):
        # this part happens no matter what was picked before(Compulsory)
        print("\nWhether you looked for it or not, the book with your name finds you eventually.")
        print("You open it. The pages describe a girl waking on cold stone. Blood on her sleeve.")
        print("A voice saying: \"You came back.\"")
        print("\nIt describes exactly what you did five minutes ago.")

        reveal_choice = choose("What do you do with this?", [
            "Keep reading — find out how the story ends",
            "Slam the book shut and refuse to know",
        ])

        if reveal_choice == 1:
            print("\nThe next blank page slowly fills with ink as you watch, writing itself in real time.")
            print('The last line, written just now: "She always wants to know how it ends."')
            self.game.set_flag("found_own_book", True)
            self.game.set_flag("accepted_truth", True)
            increase_hope(self.game, 10)
        else:
            print("\nYou shut it hard. Somewhere below, something shudders, like a held breath released.")
            self.game.set_flag("found_own_book", True)   # they still found it, just didn't read it
            increase_despair(self.game, 8)

        pause()

    def play(self):
        # just run the 3 parts in order
        self.show_intro()
        self.search_shelves()
        self.find_own_book()
        self.game.current_level = 4   # go to next level
        if 3 not in self.game.completed_levels:
            self.game.completed_levels.append(3)
        return self.game


# game calls level3(game) to match the pattern of level1, level2, level4
def level3(game):
    level = ForgottenLibrary(game)
    return level.play()