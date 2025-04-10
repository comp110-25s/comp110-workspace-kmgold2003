"""File to define Fish class."""

__author__: str = "730717858"


class Fish:
    """Defining Fish class with age attribute."""

    age: int

    def __init__(self):
        """New fish with default age 0."""
        self.age = 0
        return None

    def one_day(self):
        """Increase age of fish by 1."""
        self.age += 1
        return None
