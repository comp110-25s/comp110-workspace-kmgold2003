"""File to run river simulation."""

__author__: str = "730717858"

from exercises.EX04.river import River

my_river: River = River(10, 2)

my_river.one_river_day()

my_river.one_river_week()
