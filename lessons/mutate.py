"""Mutating functions."""

__author__ = "730395168"


def manual_append(numlist: list[int], num: int) -> None:
    """Manually appending to the list."""
    numlist.append(num)


def double(numlist: list[int]) -> None:
    """Doubling all the elements of the list."""
    x: int = 0
    while x < len(numlist):
        numlist[x] *= 2
        x += 1