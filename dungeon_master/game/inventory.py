def add_item(game, item):
    if not game.has_item(item):
        game.add_item(item)
        print(f"\n[ITEM ACQUIRED] {item}")


def show_inventory(game):
    print("\n========== INVENTORY ==========")
    if not game.inventory:
        print("Your inventory is empty.")
    else:
        for item in game.inventory:
            print(f"- {item}")
