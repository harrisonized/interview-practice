import itertools
import math


# Functions included in this file:
# # chunker
# # create_intervals
# # move_list_item_to_end
# # pairwise
# # renumerate
# # peek


def chunker(array, num_chunks=2):
    """Example:
    chunker([1, 2, 3, 4, 5, 6], 4)
    [[1, 2, 3, 4], [5, 6]]
    """
    num_groups = math.ceil(len(array)/num_chunks)

    for group_idx in range(num_groups):
        array[group_idx] = [array[group_idx]]

        try:
            for i in range(num_chunks-1):
                array[group_idx].append(array.pop(group_idx+1))
        except IndexError:
            pass  # ignore remainder

    return array


def create_intervals(start, stop, num_intervals=2):
    """Create evenly spaced intervals
    
    Example:
    create_intervals(0, 10, 5)
    [[0, 2], [2, 4], [4, 6], [6, 8], [8, 10]]
    """
    intervals = []

    interval_start, step_size = 0, (stop-start)/num_intervals
    while interval_start < stop:
        intervals.append((interval_start, interval_start+step_size))
        interval_start += step_size

    return intervals


def move_list_item_to_end(input_list: list, item):
    """Example usage:
    move_list_item_to_end([1, 2, 3, 4, 5], 3)
    [1, 2, 4, 5, 3]
    """
    output_list = input_list + [input_list.pop(input_list.index(item))]
    return output_list


def pairwise(iterable):
    """See: https://docs.python.org/3/library/itertools.html#recipes
    s -> (s0,s1), (s1,s2), (s2, s3), ...
    """
    a, b = itertools.tee(iterable)
    next(b, None)
    return list(zip(a, b))


def renumerate(sequence):
    """reverse enumerate"""
    n = len(sequence)-1
    for elem in sequence:
        yield n, elem
        n -= 1


def peek(stack): 
    if stack:
        return stack[-1] 
    return None
