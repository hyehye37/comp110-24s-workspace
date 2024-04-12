"""Testing point.py."""

__author__ = "730395168"

from lessons.CQ08.point import Point

test: Point = Point(2.0, 5.0)
test.scale_by(3)
print(test.x)
print(test.y)
test.scale_by(4)
print(test.x)
print(test.y)
