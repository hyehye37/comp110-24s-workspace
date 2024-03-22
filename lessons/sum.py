"""Summing the elements of a list using different loops."""

__author__ = "730395168"


def w_sum(vals: list[float]) -> float:
    """Return the sum using while loop."""
    idx: int = 0
    result: float = 0.0
    if len(vals) == 0:
        return 0.0
    while idx < len(vals):
        result += vals[idx] 
        idx += 1
    return result


def f_sum(vals: list[float]) -> float:
    """Return the sum using for loop."""
    result: float = 0.0
    for elem in vals:
        result += elem
    return result  


def f_range_sum(vals: list[float]) -> float:
    """Return the sum using range."""
    idx: int = 0 
    result: float = 0.0
    for idx in range(0, len(vals)):
        result += vals[idx]
    return result

    