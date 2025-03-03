"""Exercise 2: Wordle Game"""

__author__: str = "730717858"

# These are my variables for the three different emojis.
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # The user has 6 turns in the game, starting at turn 1.
    turn: int = 1
    # The variable N is the length of the argument passed
    # into the main() function so that the user is not limited
    # to only one length for their secret word.
    n: int = len(secret)
    # This while loop says that, if the string of emojis resulting from emojified()
    # is completely green (i.e., the user's guess matches the secret word perfectly),
    # then return the "win" statement.
    # Otherwise, move onto the next turn and run the while loop
    # again for a new guess.
    # After 6 attempts, the game quits with the printed "loss" statement.
    while turn < 7:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(n)
        print(emojified(guess=guess, secret=secret))
        if emojified(guess=guess, secret=secret) == GREEN_BOX * n:
            print(f"You won in {turn}/6 turns!")
            return
        turn += 1
    print("X/6 - Sorry, try again tomorrow!")


def contains_char(word: str, character: str) -> bool:
    """This function searches given word for given character"""
    assert len(character) == 1, f"len('{character}) is not 1"
    # idx stands for index. By starting its value at 0, we are
    # starting at the first letter of the string (see line 47).
    idx: int = 0
    # This while loop iterates through every letter of the given word.
    # It returns True if the letter is the same as the given character,
    # and then moves onto the next letter of the word.
    # If none of the letters match the character, it returns False.
    while idx < len(word):
        if word[idx] == character:
            return True
        idx = idx + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Test for yellow, white, or green box codification"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    # Emoji is a variable that starts an empty string. The while
    # loop adds a new emoji onto the end of the string in each iteration.
    emoji: str = ""
    idx: int = 0
    # This while loop iterates through each letter of the user's guess.
    # For every letter, it  calls the contains_char function.
    # In the if statement, the function call looks specifically
    # at the first letter of the secret word, and the first letter
    # of the guess. If they are the same, the function will return
    # True, and then a Green Box will be added to the emoji string.
    # If not (elif), the function call then looks at the first
    # letter of the guess and sees if it is contained anywhere in
    # the secret word. If it is, it will return True, and a Yellow Box
    # will be added to the emoji string. If the first letter of the guess
    # is not found anywhere in the secret word (else), then a White Box is added.
    # This process repeats for every letter in the guess to form an
    # emoji that is the same length as the guess, telling the user
    # which letters from the guess are in the right spot of the secret word (Green Box),
    # which letters are in the secret word but are in the wrong spot (Yellow Box),
    # and which letters are not in the secret word at all (White Box).
    while idx < len(guess):
        if contains_char(word=secret[idx], character=guess[idx]):
            emoji = emoji + GREEN_BOX
        elif contains_char(word=secret, character=guess[idx]):
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
        idx = idx + 1
    return emoji


def input_guess(n: int) -> str:
    """Prompt user for a guess of the expected length"""
    # The word variable is a string whose initial value is the
    # word inputted by the user when prompted. Observe that this word,
    # after this function call is completed, ends up being the user's guess
    # in the main() function call (see line 27).
    word: str = input(f"Enter a {n} character word:")
    # This while loop ensures that the length of the inputted
    # word is the same as the length N specified in the function
    # call. As long as they are not the same length, the
    # user will be prompted for a new word, whose value
    # will be assigned to the word variable, replacing
    # its previous value. This loop is ended once the user's word is of length N,
    # and then the word is returned to wherever the function was called (see line 27).
    while len(word) != n:
        word = input(f"That wasn't {n} chars! Try again:")
    return word


# These 2 lines make it possible for this program to run as a module and for
# other modules to import the above functions and reuse them.
if __name__ == "__main__":
    main(secret="codes")
