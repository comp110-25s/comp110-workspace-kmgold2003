"""Exercise 3: Dictionary"""

__author__: str = "730717858"


def invert(og: dict[str, str]) -> dict[str, str]:
    """Invert keys and values"""
    new: dict[str, str] = {}
    for key in og:
        if og[key] in new:
            raise KeyError("Key value cannot be used more than once!")
        else:
            new[og[key]] = key
    return new


def count(lst: list[str]) -> dict[str, int]:
    """Counts number of times value appears in input list"""
    result: dict[str, int] = {}
    idx: int = 0
    while idx < len(lst):
        if lst[idx] in result:
            result[lst[idx]] += 1
        else:
            result[lst[idx]] = 1
        idx += 1
    return result


def favorite_color(colors: dict[str, str]) -> str:
    """Counts frequency of colors to find favorite"""
    result: str = ""
    lst: list[str] = []
    freq: dict[str, int] = {}
    num: int = 0
    for name in colors:
        lst.append(colors[name])
    freq = count(lst)
    for color in freq:
        if freq[color] > num:
            result = color
            num = freq[color]
    return result


def bin_len(lst: list[str]) -> dict[int, set[str]]:
    """Bins list of strings into dictionary keyed by length of string"""
    result: dict[int, set[str]] = {}
    idx: int = 0
    while idx < len(lst):
        length = len(lst[idx])
        if length in result:
            result[length].add(lst[idx])
        else:
            result[length] = {lst[idx]}
        idx += 1
    return result
