def increase_hope(game, amount):
    old = game.heart_gem
    game.change_heart(abs(amount))
    print(f"\n[HOPE +{game.heart_gem - old}] Heart Gem: {game.heart_gem}/100")


def increase_despair(game, amount):
    old = game.heart_gem
    game.change_heart(-abs(amount))
    print(f"\n[DESPAIR +{old - game.heart_gem}] Heart Gem: {game.heart_gem}/100")


def is_corrupted(game):
    return game.heart_gem <= 0
