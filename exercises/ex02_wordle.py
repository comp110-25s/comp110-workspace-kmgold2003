"""Exercise 2: Wordle Game"""

__author__: str = "730717858"

# These are my variables for the three different emojis.
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    # The variable N is defined as the length of the argument passed
    # into the main() function so that the user is not limited
    # to only one length for their secret word.
    N: int = len(secret)
    # This while loop says that, if the string of emojis resulting from emojified()
    # is completely green (N green boxes), then return the "win" statement.
    # Otherwise, increase the turn value by 1 and run the while loop
    # again for a new guess.
    while turn < 7:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(N)
        print(emojified(guess=guess, secret=secret))
        if emojified(guess=guess, secret=secret) == GREEN_BOX * N:
            print(f"You won in {turn}/6 turns!")
            return
        turn += 1
    print("X/6 - Sorry, try again tomorrow!")


def contains_char(word: str, character: str) -> bool:
    """This function searches given word for given character"""
    assert len(character) == 1, f"len('{character}) is not 1"
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
    # Emoji is initialized as an empty string where the while
    # loop adds a new emoji onto the end of the string in each iteration
    emoji: str = ""
    idx: int = 0
    # This while loop iterates through each letter of the guess.
    # For every letter, it  calls the contains_char function.
    # In the if statement, the function call looks specifically
    # at the first letter of the secret word, and the first letter
    # of the guess. If they are the same, the function will return
    # True, and then a Green Box will be added to the emoji string.
    # In the elif statement, the function call looks at the first
    # letter of the guess and sees if it is contained anywhere in
    # the secret. If it is, it will return True, and a Yellow Box
    # will be added to the emoji string. The else statement means
    # that the first letter of the guess was not found anywhere in
    # the secret word, so a White Box is added. This process is
    # iterated for every letter in the guess to form an emoji
    # that is the same length as the guess.
    while idx < len(guess):
        if contains_char(word=secret[idx], character=guess[idx]) == True:
            emoji = emoji + GREEN_BOX
        elif contains_char(word=secret, character=guess[idx]) == True:
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
        idx = idx + 1
    return emoji


def input_guess(N: int) -> str:
    """Prompt user for a guess of the expected length"""
    # The word variable is initialized as the string
    # inputted by the user.
    word: str = input(f"Enter a {N} character word:")
    # This while loop ensures that the length of the inputted
    # word is the same as the specified length N in the function
    # call. As long as they are NOT the same length, the
    # user will be prompted for a new word, whose value
    # will be assigned to the word variable, thereby
    # replacing its previous value. This loop is
    # escaped once word is of length N, and then word
    # is returned to wherever the function is called.
    while len(word) != N:
        word = input(f"That wasn't {N} chars! Try again:")
    return word


if __name__ == "__main__":
    main(secret="codes")
