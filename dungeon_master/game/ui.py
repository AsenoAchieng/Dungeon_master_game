import os
import sys
import time


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause(message="Press Enter to continue..."):
    input(f"\n{message}")


def slow_print(text, delay=0.0):
    # delay can be increased later for a cinematic typewriter effect.
    for line in text.splitlines():
        print(line)
        if delay:
            time.sleep(delay)


def title(text):
    print("\n" + "=" * 62)
    print(text.center(62))
    print("=" * 62)


def heart_bar(value):
    filled = round(value / 5)
    empty = 20 - filled
    return "♥" * filled + "·" * empty


def show_status(game):
    print(f"\nHeart Gem: [{heart_bar(game.heart_gem)}] {game.heart_gem}/100")
    if game.inventory:
        print("Inventory:", ", ".join(game.inventory))
    else:
        print("Inventory: Empty")


def choose(prompt, options):
    while True:
        print(f"\n{prompt}")
        for number, option in enumerate(options, start=1):
            print(f"  {number}. {option}")
        answer = input("\n> ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return int(answer)
        print("Please enter a valid option number.")


def ask_yes_no(prompt):
    while True:
        answer = input(f"{prompt} (y/n): ").strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please enter y or n.")
