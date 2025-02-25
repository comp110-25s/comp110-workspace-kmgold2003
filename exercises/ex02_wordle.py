"""Exercise 2: Wordle Game"""

__author__: str = "730717858"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, character: str) -> bool:
    """This function searches given word for given character"""
    assert len(character) == 1, f"len('{character}) is not 1"
    idx: int = 0
    while idx < len(word):
        if word[idx] == character:
            return True
        idx = idx + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """This function calls upon contains_char() to test for yellow or white box codification"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    emoji: str = ""
    idx: int = 0
    while contains_char(word=guess, character=secret[idx]):
        idx = idx + 1
        return


def input_guess(N: int) -> str:
    """Given an integer of expected length of a guess, this function prompts the user for a guess of the expected length"""
    word = input(f"Enter a {N} character word:")
    while len(word) != N:
        return f"That wasn't {N} chars! Try again:"

    return word
