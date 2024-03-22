"""QUIZ02 Practice Problems"""


def odd_and_even(input: list[int]) -> list[int]:
    """Return a new list with elements that are odd and have even index."""
    idx: int = 0
    new_list: list[int] = []
    while idx < len(input):
        if input[idx] % 2 == 1 and idx % 2 == 0:
            new_list.append(input[idx])
        idx += 1
    return new_list
    

def short_words(my_list: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    idx: int = 0
    new_list: list[int] = []
    while idx < len(my_list):
        if len(my_list[idx]) < 5:
            new_list.append(my_list[idx])
            idx += 1   
        else:
            return (f"{my_list[idx]} is too long!")
        print(new_list)


def value_exists(dict: dict[str,int], val: int) -> bool:
 """The function returns True if the int exists as a value in the dictionary, and False otherwise."""
 for key in dict:
    if dict[key] == val:
        return True
 return False