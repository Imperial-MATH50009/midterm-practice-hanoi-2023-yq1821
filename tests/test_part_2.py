import pytest
try:
    from hanoi.hanoi import Game
except ImportError:
    pass


def test_hanoi_import():
    from hanoi.hanoi import Game


@pytest.mark.parametrize("disks, stack", [
    (3, [3, 2, 1]),
    (5, [5, 4, 3, 2, 1]),
    (-1, [])
])
def test_stack(disks, stack):
    from hanoi.hanoi import Game
    assert Game(disks).stack(0) == stack
