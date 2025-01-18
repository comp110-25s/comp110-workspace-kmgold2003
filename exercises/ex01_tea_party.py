"""Exercise 1: Planning a Tea Party Based on Number of Attendees"""

__author__: str = "730717858"


def main_planner(guests: int) -> None:
    """Plans my tea party based on number of guests"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Determines number of tea bags based on number of guests"""
    return people * 2


def treats(people: int) -> int:
    """Determines number of treats based on number of treats"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Determines cost of the teabags and treats combined"""
    return (tea_count) * 0.50 + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
