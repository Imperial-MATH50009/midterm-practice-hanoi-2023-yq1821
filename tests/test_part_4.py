import pytest


def test_standard_move():
    from hanoi.hanoi import Game
    g = Game(3)
    g.move(0, 2)
    g.move(0, 1)
    assert(g.stack(0), g.stack(1), g.stack(2)) == ([3], [2], [1]), \
        "expected stacks of 0:[3], 1:[2], 2:[1]"


@pytest.fixture
def base_game():
    """Return game state ((0, [4, 3]), (1, [2, 1]))."""
    from hanoi.hanoi import Game
    g = Game(4)
    g.move(0, 1)
    g.move(1, 2)
    g.move(0, 1)
    g.move(2, 1)
    return g


def empty_move(base_game):
    g = base_game
    g.move(2, 1)


def wrong_size_move(base_game):
    g = base_game
    g.move(0, 1)


def test_empty_move(base_game):
    with pytest.raises(ValueError, match=r"Stack .* is empty"):
        empty_move(base_game)


def test_wrong_size_move(base_game):
    with pytest.raises(ValueError, match=r"Cannot place disc .* on disc .*."):
        wrong_size_move(base_game)


def test_game_state(base_game):
    g = base_game
    stack = g.stack(0)
    try:
        g.move(0, 1)
    except ValueError:
        assert g.stack(0) == stack, \
            "expected unchanged stack after wrong move"
