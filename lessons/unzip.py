"""Splitting a dictionary into two lists."""

__author__ = "730395168"


def get_keys(test_dict: dict[str, int]) -> list[str]: 
    """Print all the keys in test_dict."""
    list1: list[str] = []
    if len(test_dict) == 0:
        return []
    for key in test_dict:
        if test_dict[key]:
            list1.append(key)
    return list1 
    

def get_values(test_dict: dict[str, int]) -> list[int]: 
    """Print all the values in test_dict."""
    list1: list[int] = []
    if len(test_dict) == 0:
        return []
    for key in test_dict:
        if test_dict[key]:
            list1.append(test_dict[key])
    return list1