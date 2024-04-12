"""Functions that implement sorting algorithms."""

__author__ = "730395168"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list."""
    idx_unsorted: int = 0
    while idx_unsorted < len(x): 
        idx_sorted: int = idx_unsorted - 1
        current_num: int = idx_unsorted
        while idx_unsorted > 0 and idx_sorted >= 0: 
            if x[current_num] < x[idx_sorted]:
                temp = x[current_num]
                x[current_num] = x[idx_sorted]
                x[idx_sorted] = temp
                current_num = idx_sorted
            idx_sorted -= 1
        idx_unsorted += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    current_idx: int = 0
    while current_idx < len(x):
        idx_unsorted = current_idx
        min_idx = current_idx
        while idx_unsorted < len(x):
            if x[idx_unsorted] < x[min_idx]:
                min_idx = idx_unsorted
                idx_unsorted += 1 
            else:
                idx_unsorted += 1
        temp_int = x[current_idx]
        x[current_idx] = x[min_idx]
        x[min_idx] = temp_int
        current_idx += 1
    return None