"""Exercise 3: Dictionary Test"""

__author__: str = "730717858"

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count


def test_invert() -> None:
    """Tests invert function"""
    assert invert({"kitty": "goldman"}) == {"goldman": "kitty"}
    assert invert({"a": "alpha", "b": "beta", "c": "gamma", "d": "delta"}) == {
        "alpha": "a",
        "beta": "b",
        "gamma": "c",
        "delta": "d",
    }
    assert invert({"": ""}) == {"": ""}


def test_count() -> None:
    """Tests count function"""
    assert count(["a", "a", "b", "c", "c", "c"]) == {"a": 2, "b": 1, "c": 3}
    assert count(["k", "i", "t", "t", "y"]) == {"k": 1, "i": 1, "t": 2, "y": 1}
    assert count([]) == {}
