"""Testing functions in garden_helpers."""

__author__ = "730395168"

from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_add_by_kind_new() -> None:
    """Returns the list with the new plant kind and corresponding plant."""
    kind: str = "herb"
    plant: str = "parsley"
    test: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    add_by_kind(test, kind, plant)
    assert test == {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"], "herb": ["parsley"]}


def test_add_by_kind_empty() -> None:
    """Returns the statement <month> is not a kind of plant."""
    kind: str = "flower"
    plant: str = "zinnia"
    test: dict[str, list[str]] = {}
    add_by_kind(test, kind, plant) 
    assert test == {"flower": ["zinnia"]}


def test_add_by_date_new() -> None:
    """If there is not already a month in the <garden_by_date>, add the month and corresponding plant."""
    month: str = "February"
    plant: str = "orchid"
    test: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    add_by_date(test, month, plant)
    assert test == {"April": ["marigold"], "June": ["carrots"], "February": ["orchid"]}


def test_add_by_date_empty() -> None:
    """Returns the statement <plant_kind> is not a month."""
    month: str = "April"
    plant: str = "marigold"
    test: dict[str, list[str]] = {}
    add_by_date(test, month, plant) 
    assert test == {"April": ["marigold"]}


def test_lookup_by_kind_and_date_fruit() -> None: 
    """Returns the statement <kind> to plant in <month>: [plant name]."""
    kind: str = "fruit"
    month: str = "August"
    test_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"], "fruit": ["watermelon"]}
    test_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"], "August": ["watermelon"]}
    assert lookup_by_kind_and_date(test_kind, test_date, kind, month) == f"{kind} to plant in {month}: ['watermelon']."


def test_lookup_by_kind_and_date_herb() -> None:
    """Returns "No {kind} to plant in {month}."""
    kind: str = "herb"
    month: str = "June"
    test_kind: dict[str, list[str]] = {"herb": ["basil"], "flower": ["marigold", "zinnia"], "vegetable": ["carrots"], "fruit": ["watermelon"]}
    test_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"], "August": ["watermelon"]}
    assert lookup_by_kind_and_date(test_kind, test_date, kind, month) == f"No {kind} to plant in {month}."