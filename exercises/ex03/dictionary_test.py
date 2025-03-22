"""Exercise 3: Dictionary Test"""

__author__: str = "730717858"

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len


def test_invert_1() -> None:
    """Tests invert function"""
    assert invert({"kitty": "goldman"}) == {"goldman": "kitty"}


def test_invert_2() -> None:
    """Tests invert function"""
    assert invert({"a": "alpha", "b": "beta", "c": "gamma", "d": "delta"}) == {
        "alpha": "a",
        "beta": "b",
        "gamma": "c",
        "delta": "d",
    }


def test_invert_3() -> None:
    """Tests invert function"""
    assert invert({"": ""}) == {"": ""}


def test_count_1() -> None:
    """Tests count function"""
    assert count(["a", "a", "b", "c", "c", "c"]) == {"a": 2, "b": 1, "c": 3}


def test_counts_2() -> None:
    """Tests count function"""
    assert count(["k", "i", "t", "t", "y"]) == {"k": 1, "i": 1, "t": 2, "y": 1}


def test_counts_3() -> None:
    """Tests count function"""
    assert count([]) == {}


def test_favorite_color_1() -> None:
    """Tests favorite color function"""
    assert favorite_color({"mom": "green", "dad": "green", "kitty": "blue"}) == "green"


def test_favorite_color_2() -> None:
    """Tests favorite color function"""
    assert (
        favorite_color(
            {"alex": "blue", "bill": "pink", "david": "blue", "john": "pink"}
        )
        == "blue"
    )


def test_favorite_color_3() -> None:
    """Tests favorite color function"""
    assert favorite_color({}) == ""


def test_bin_len_1() -> None:
    """Tests bin function"""
    assert bin_len(["unc", "beat", "duke"]) == {3: {"unc"}, 4: {"beat", "duke"}}


def test_bin_len_2() -> None:
    """Tests bin function"""
    assert bin_len(["who", "what", "where", "When", "Why"]) == {
        3: {"who", "Why"},
        4: {"what", "When"},
        5: {"where"},
    }


def test_bin_len_3() -> None:
    """Tests bin function"""
    assert bin_len([]) == {}
