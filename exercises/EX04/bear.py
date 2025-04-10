"""File to define Bear class."""

__author__: str = "730717858"


class Bear:
    """Defining Bear class with age and hunger_score attributes."""

    age: int
    hunger_score: int

    def __init__(self):
        """New bear with default age  0 and default hunger score 0."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Increase age of bear by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Increase hunger score of bear by number of fish."""
        self.hunger_score += num_fish
        return None
