"""Writing A Recursive Function."""

__author__ = "730395168"


def f(n: int, k: int) -> int:
    """Recursive definition for the function f."""
    if n == 0:
        return 0 
    else:
        return f(n - 1, k) + (1 * k)