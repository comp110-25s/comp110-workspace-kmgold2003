"""File to define River class."""

__author__: str = "730717858"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """Defining River class with day, bears, and fish attributes."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Check age of bear and fish and remove if too old."""
        bears_alive: list[Bear] = []
        fish_alive: list[Fish] = []
        for bear in self.bears:
            if bear.age <= 5:
                bears_alive.append(bear)
        for fish in self.fish:
            if fish.age <= 3:
                fish_alive.append(fish)
        self.bears = bears_alive
        self.fish = fish_alive
        return None

    def remove_fish(self, amount: int) -> None:
        """Remove specified amount of fish from river."""
        count: int = 0
        while count < amount:
            self.fish.pop(0)
            count += 1
        return None

    def bears_eating(self):
        """Bear will eat 3 fish if 5 fish are available."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Check hunger score of bear."""
        bears_alive: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                bears_alive.append(bear)
        self.bears = bears_alive

        return None

    def repopulate_fish(self):
        """Each pair of fish produces 4 offspring."""
        offspring: int = (len(self.fish) // 2) * 4
        count: int = 1
        while count <= offspring:
            fish: Fish = Fish()
            self.fish.append(fish)
        return None

    def repopulate_bears(self):
        """Each pair of bears produces 1 offspring."""
        offspring: int = len(self.bears) // 2
        count: int = 1
        while count <= offspring:
            bear: Bear = Bear()
            self.bears.append(bear)
        return None

    def view_river(self):
        """View current status of river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        days_run: int = 0
        while days_run < 7:
            self.one_river_day()
            days_run += 1
        return None
