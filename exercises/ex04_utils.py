"""list Utility Functions."""

__author__ = "730395168"


def all(numlist: list[int], num: int) -> bool:
    """Indicate whether or not all the ints in the list are the same as the given int."""
    idx: int = 0
    if len(numlist) == 0:
        return False
    while idx < len(numlist):
        if numlist[idx] != num:
            return False 
        idx += 1
    return True 


def max(input: list[int]) -> int:
    """Return the max number from the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    idx: int = 0
    max_num: int = input[0]
    while idx < len(input):
        current_num: int = input[idx]
        if current_num > max_num:
            max_num = current_num
        idx += 1
    return max_num


def is_equal(L1: list[int], L2: list[int]) -> bool:
    """Determine if the two lists are the same or not."""
    idx: int = 0
    if len(L1) != len(L2):
        return False
    while idx < len(L1):
        if L1[idx] != L2[idx]: 
            return False 
        idx += 1
    return True 
        

def extend(L1: list[int], L2: list[int]) -> None:
    """Mutate L1 by appending L2."""
    idx: int = 0
    while idx < len(L2):
        L1.append(L2[idx])
        idx += 1