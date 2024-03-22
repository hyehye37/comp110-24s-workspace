"""Dictionary Functions."""

__author__ = "730395168"


def invert(test_dict: dict[str, str]) -> dict[str, str]: 
    """Invert the keys and values."""
    reversed_dict: dict[str, str] = {}
    for key in test_dict: 
        if test_dict[key] in reversed_dict:
            raise KeyError("Duplicate Key")
        else:
            reversed_dict[test_dict[key]] = key
    return reversed_dict


def favorite_color(color_pref: dict[str, str]) -> str:
    """Return the most popular color."""
    new_dict: dict[str, int] = {}
    for name in color_pref:
        if color_pref[name] in new_dict:
            new_dict[color_pref[name]] += 1
        else: 
            new_dict[color_pref[name]] = 1
    max_color: str = ""
    max_num: int = 0
    for color in new_dict:
        if new_dict[color] > max_num:
            max_color = color
            max_num = new_dict[color]
    return max_color


def count(val: list[str]) -> dict[str, int]:
    """Count of the number of times a value appeared in the list."""
    result: dict[str, int] = {}
    idx: int = 0
    while idx < len(val):
        if val[idx] in result: 
            result[val[idx]] += 1
        else: 
            result[val[idx]] = 1
        idx += 1
    return result


def alphabetizer(words_list: list[str]) -> dict[str, list[str]]:
    """Return the alpahbet and the words in the list."""
    sort: dict[str, list[str]] = {}
    for word in words_list:
        if word[0] not in sort:
            sort[word[0]] = [word.lower()]
        else:
            sort[word[0]].append(word.lower())
    return sort


def update_attendance(attendance_log: dict[str, list[str]], day: str, attendee: str) -> None:
    """Update the existing dict and return it."""
    if day in attendance_log:
        if attendee not in attendance_log[day]:
            attendance_log[day].append(attendee)
    else: 
        attendance_log[day] = [attendee]