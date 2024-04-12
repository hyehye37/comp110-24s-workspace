"""Create and compare two similar methods."""

from __future__ import annotations

__author__ = "730395168"


class Point:
    """CQ08 class Point."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Defining a constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Method to mutate Point."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Creating a new Point."""
        return Point(self.x * factor, self.y * factor)