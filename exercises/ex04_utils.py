<<<<<<< HEAD
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
=======
"""List utils."""

__author__ = 720310785

def all(inp: list[int], val: int) -> bool:
    """Tell if list is all one number."""
    idx: int = 0
    while idx < len(inp):
        if val != inp[idx]:
            return False
        idx += 1
    return True

def max(inp: list[int]) -> int:
    """Find max in list."""
    idx: int = 0
    if len(inp) == 0:
        raise ValueError("max() arg is an empty List")
    max_num: int = inp[0]
    while idx < len(inp):
        if inp[idx] > max_num:
            max_num = inp[idx]
        idx += 1
    return max_num

def is_equal(inp1: list[int], inp2: list[int]) -> bool:
    """Check if two lists are equal."""

    if len(inp1) != len(inp2):
        return False
    else:
        idx: int = 0
        while idx < len(inp1):
            if inp1[idx] != inp2[idx]:
                return False
            idx += 1
    return True

def extend(inp1: list[int], inp2: list[int]) -> None:
    idx: int = 0
    while idx < len(inp2):
        inp1.append(inp2[idx])
        idx += 1
>>>>>>> 2ef5de78e346e7cf4170e08810c73ab71f3465a1
