"""Unit tests for functions from ex05."""

__author__ = "730395168"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_one() -> None:
    """Returns the inverted key and value of a dict that has only one pair of key and value."""
    test: dict[str, str] = {"apple": "cat"}
    assert invert(test) == {"cat": "apple"}


def test_invert_multi() -> None:
    """Returns the inverted keys and values of a dict with multiple sets of keys and values."""
    test: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    assert invert(test) == {"z": "a", "y": "b", "x": "c"}


def test_invert_empty() -> None:
    """Retunrs an empty dict if the input dict is empty."""
    test: dict[str, str] = {}
    assert invert(test) == {}


def test_favorite_color_one() -> None:
    """Returns the color in the dict that has only one pair of key and value."""
    test: dict[str, str] = {"Marc": "yellow"}
    assert favorite_color(test) == "yellow"


def test_favorite_color_multi() -> None:
    """Returns the most popular color in the dict with multiple pairs of keys and values."""
    test: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(test) == "blue"


def test_favorite_color_double() -> None:
    """Returns the first color that appears in the dict if two or more colors are tied."""
    test: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Julie": "yellow", "Jack": "red"}
    assert favorite_color(test) == "yellow"


def test_count_once() -> None:
    """When all the items in the list show up only once."""
    test: list[str] = ["apple", "banana", "orange"]
    assert count(test) == {"apple": 1, "banana": 1, "orange": 1}


def test_count_default() -> None:
    """Default output of the function - returning the dict of the item with its count."""
    test: list[str] = ["apple", "banana", "orange", "apple", "apple", "orange"]
    assert count(test) == {"apple": 3, "banana": 1, "orange": 2}


def test_count_empty() -> None:
    """If the input is an empty list, return an empty dict."""
    test: list[str] = []
    assert count(test) == {}


def test_alphabetizer_one() -> None:
    """One word for each alphabet."""
    test: list[str] = ["cat", "apple", "boy"]
    assert alphabetizer(test) == {"c": ["cat"], "a": ["apple"], "b": ["boy"]}


def test_alphabetizer_upper_case() -> None:
    """Input strings with uppercases."""
    test: list[str] = ["Python", "sugar", "Turtle", "party", "table"]
    assert alphabetizer(test) == {'p': ['Python', 'party'], 's': ['sugar'], 't': ['Turtle', 'table']}


def test_alphabetizer_empty() -> None:
    """When the input list is empty return empty dict."""
    test: list[str] = []
    assert alphabetizer(test) == {}


def test_update_attedance_default() -> None:
    """Correct mutation."""
    test_dict: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day: str = "Tuesday"
    name: str = "Vrinda"
    update_attendance(test_dict, day, name)
    assert test_dict == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Vrinda"]}


def test_update_attendance_no_repeat() -> None:
    """No same names in the same day."""
    test_dict: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    day: str = "Monday"
    name: str = "Kaleb"
    update_attendance(test_dict, day, name)
    assert test_dict == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}


def test_update_attendance_empty() -> None:
    """Empty dict."""
    test_dict: dict[str, list[str]] = {}
    day: str = "Monday"
    name: str = "Kaleb"
    update_attendance(test_dict, day, name)
    assert test_dict == {'Monday': ['Kaleb']}