"""Exercise 3: Dictionary Test"""

__author__: str = "730717858"

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len


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


def test_favorite_color() -> None:
    """Tests favorite color function"""
    assert favorite_color({"mom": "green", "dad": "green", "kitty": "blue"}) == "green"
    assert (
        favorite_color(
            {"alex": "blue", "bill": "pink", "david": "blue", "john": "pink"}
        )
        == "blue"
    )
    assert favorite_color({}) == ""


def test_bin_len() -> None:
    """Tests bin function"""
    assert bin_len(["unc", "beat", "duke"]) == {3: {"unc"}, 4: {"beat", "duke"}}
    assert bin_len(["who", "what", "where", "When", "Why"]) == {
        3: {"who", "Why"},
        4: {"what", "When"},
        5: {"where"},
    }
    assert bin_len([]) == {}
