from copy import deepcopy
from collections import defaultdict, deque
import random
from ..structs.tree import binary_tree_from_array, bucketer
from ..math.numbers import get_digit, digits_num_to_tuple, digits_tuple_to_num


# Functions
# # idx_hash_table_for_array
# # map_hash

# # bubble_sort
# # selection_sort
# # insertion_sort
# # counting_sort
# # tree_sort

# # merge_sort
# # bucket_sort
# # radix_sort_v0
# # radix_sort

# # qs_partition
# # quick_sort


def idx_hash_table_for_array(array):
    """ returns a dictionary with ids as keys and a list of indexes as values """
    
    hash_table = {}
    for original_idx, num in enumerate(array):
        if hash_table.get(id(num)) is None:
            hash_table[id(num)] = deque([original_idx])
        else:
            hash_table[id(num)].append(original_idx)

    return hash_table


def map_hash(array, hash_table):
    """Returns original positions of a sorted array
    Use in conjunction with idx_hash_table_for_array
    """
    temp_hash_table = deepcopy(hash_table)  # preserve original copy
    return [temp_hash_table[id(num)].popleft() for num in array]


def bubble_sort(array: list, to_print=False):
    """Sorts in-place
    
    Example:
    array = [64, 34, 25, 12, 22, 11, 90]
    
    During each loop, traverse from 1 to n-l, where l is the loop number
    Keep track of curr_num and prev_num
    If prev_num > curr_num, swap them
    
    l, pn, array
    0, 90, [34, 25, 12, 22, 11, 64, 90]
    1, 64, [25, 12, 22, 11, 34, 64, 90]
    2, 34, [12, 22, 11, 25, 34, 64, 90]
    3, 25, [12, 11, 22, 25, 34, 64, 90]
    4, 22, [11, 12, 22, 25, 34, 64, 90]
    5, 12, [11, 12, 22, 25, 34, 64, 90]
    6, 11, [11, 12, 22, 25, 34, 64, 90]
    """
    array_len = len(array)

    for loop_idx in range(array_len):
        
        prev_num = array[0]  # skip first index, look backward
        for i, curr_num in enumerate(array[1:array_len-loop_idx], 1):

            if prev_num > curr_num:
                array[i-1], array[i] = array[i], array[i-1]  # swap
                curr_num = prev_num  # swap

            prev_num = curr_num
            
        print(loop_idx, prev_num, array) if to_print else None
        
    return array


def selection_sort(array: list, to_print=False):
    """Sorts in-place
    
    Example:
    array = [64, 34, 25, 12, 22, 11, 90]
    
    During each loop from l to n, find minimum and swap with first element of loop
    
    l, mi, array
    0, 11, [64, 34, 25, 12, 22, 11, 90]
    1, 12, [11, 34, 25, 12, 22, 64, 90]
    2, 22, [11, 12, 25, 34, 22, 64, 90]
    3, 25, [11, 12, 22, 34, 25, 64, 90]
    4, 34, [11, 12, 22, 25, 34, 64, 90]
    5, 64, [11, 12, 22, 25, 34, 64, 90]
    6, 90, [11, 12, 22, 25, 34, 64, 90]
    """
    array_len = len(array)
    
    for loop_idx in range(array_len):
        
        min_idx, prev_num = loop_idx, array[loop_idx]
        for i, curr_num in enumerate(array[1+loop_idx:], 1+loop_idx):
            
            if curr_num < prev_num:
                min_idx = i
                
            prev_num = curr_num
            
        print(loop_idx, array[min_idx], array) if to_print else None
        array[loop_idx], array[min_idx] = array[min_idx], array[loop_idx]
        
    return array


def insertion_sort(array: list, to_print=False):
    """Sorts in-place
    
    Example:
    array = [64, 34, 25, 12, 22, 11, 90]
    
    l, ln, 
    0, [64, 34, 25, 12, 22, 11, 90]
    compare 34 and 64, 34 < 64 so array[0] = 34 and array[1] = 64
    
    1, [34, 64, 25, 12, 22, 11, 90]
    compare 25 and 34, 25 < 34 so array[0] = 25, array[1] = 34, array[2] = 64
    
    2, [25, 34, 64, 12, 22, 11, 90]
    compare 12 and 25, 12 < 25, so array[0] = 12, array[1] = 25, array[2] = 34, array[3] = 64
    
    3, [12, 25, 34, 64, 22, 11, 90]
    compare 22 and 12, 22 > 12 so skip. 22 < 25, so array[1] = 22, array[2] = 25, array[3] = 34, array[4] = 64

    4, [12, 22, 25, 34, 64, 11, 90]
    5, [11, 12, 22, 25, 34, 64, 90]
    
    During each loop from l to n, array[0:l] is considered sorted.
    Move the next element to the appropriate position in the sorted part.
    """
    array_len = len(array)
    
    for loop_idx in range(1, array_len):
        
        insert_num = array[loop_idx]

        for i, curr_num in enumerate(array[0:loop_idx]):
            
            print(loop_idx, insert_num, curr_num, array)  if to_print else None
            if insert_num < curr_num:
                array[i], insert_num = insert_num, curr_num
                
        array[i+1] = insert_num
        
    return array


def counting_sort(array: list):
    """Can only use if range and spacing is known 
    Build a dictionary with num as keys and count as values
    Iterate through the known range, retrieving counts from the dictionary
    Use deque because append operation is O(1)
    This doesn't preserve the original items
    
    Runtime is O(n+range)
    """
    
    # these would normally be arguments
    array_min, array_max = min(array), max(array)
    
    # this can also be implemented as
    # counter = Counter(array)
    counter = defaultdict(dict)
    for num in array:
        if counter.get(num) is None:
            counter[num] = 1
        else:
            counter[num] += 1
    
    new_array = deque([])
    for num in range(array_min, array_max+1):
        count = counter.get(num)
        if count is not None:
            for iterations in range(count):
                new_array.append(num)
    
    return list(new_array)


def tree_sort(array):
    """Sort by insertion into binary tree
    
    Example:
    tree_sort([4, 10, 3, 5, 1])
    [1, 3, 4, 5, 10]
    """
    
    tree = binary_tree_from_array(array)
    for i, node in enumerate(tree.recursive_inorder()):
        array[i] = node.data
        
    return array


def merge_sort(array, to_print=False):
    """Recursively calls itself to split
    Then reconstructs a new sorted array during the merging process
    
    Eg. 
    array = [12, 11, 13, 5, 6, 7]
    array = merge_sort(array)
    array
    
    [5, 6, 7, 11, 12, 13]

    Should look up iterative implementation
    See: https://stackoverflow.com/questions/18761766/mergesort-with-python
    """
    if len(array) > 1:
        
        # split
        mid = len(array)//2
        left, right = array[:mid], array[mid:]
        print("split: ", array, left, right) if to_print else None
        
        # recursive call
        left = merge_sort(left)
        right = merge_sort(right)
        
        # update input array with sorted elements
        i = 0  # array_idx
        while len(left) != 0 and len(right) != 0:
            if left[0] < right[0]:
                array[i] = left.pop(0)
            else:
                array[i] = right.pop(0)
            i += 1
        
        # copy missed elements
        print("remain: ", i, left, right)  if to_print else None
        if left:
            for num in left:
                array[i] = num
                i += 1
        if right:
            for num in right:
                array[i] = num
                i += 1
                
    print("merge: ", array)  if to_print else None
    return array


def bucket_sort(array, intervals, sorter=bubble_sort, to_print=False):
    """Group input array into buckets, sort each bucket, then merge
    The bucketer algorithm relies on binary search tree
    
    Example:
    bucket_sort([64, 34, 25, 12, 22, 11, 90], [(0, 25.0), (25.0, 50.0), (50.0, 75.0), (75.0, 100.0)])
    
    bucketer([64, 34, 25, 12, 22, 11, 90], [(0, 25.0), (25.0, 50.0), (50.0, 75.0), (75.0, 100.0)])
    [[12, 22, 11], [34, 25], [64], [90]]
    
    buckets = [[12, 22, 11], [34, 25], [64], [90]]  # sort each bucket, then merge
    return [11, 12, 22, 25, 34, 64, 90]
    """
    
    buckets = bucketer(array, intervals)
    print(buckets) if to_print else None
    
    for bucket in buckets:
        bucket = sorter(bucket)

    return [num for bucket in buckets for num in bucket]  # unpack buckets


def radix_sort_v0(array):
    """ Sort each decimal place, then join
    The implementation is bad, but logic is correct.
    
    In order to make a better implementation, would need to write
    a counting_sort algorithm that enables python to preserve index of sorted items
    
    Example:
    [1, 203, 10, 14]  # input
    [10, 1, 203, 14]  # sort 1's place first pass
    [1, 203, 10, 14]  # sort 10's place second pass
    [1, 10, 14, 203]  # sort 100's place first
    """
    max_num = max(array)
    num_digits = len(str(max_num))
    
    digitized_array = [digits_num_to_tuple(num, num_digits) for num in array]
    
    for digit in range(num_digits):
        digitized_array = sorted(digitized_array, key=lambda x: x[digit])
        
    return [digits_tuple_to_num(digits) for digits in digitized_array]


def radix_sort(array, to_print=False):
    """ Sort each decimal place, then join
    Like bucket_sort, but for each decimal place
    Use hashtables to preserve original object
    
    Example:
    array = [1, 203, 10, 14]
    radix_sort(array)
    
    {1: deque([1]), 0: deque([10]), 4: deque([14]), 3: deque([203])}
    [10, 1, 203, 14]
    {1: deque([10, 14]), 0: deque([1, 203])}
    [1, 203, 10, 14]
    {0: deque([1, 10, 14]), 2: deque([203])}
    [1, 10, 14, 203]
    {0: deque([1, 10, 14, 203])}
    [1, 10, 14, 203]
    """
    max_num = max(array)
    num_digits = len(str(max_num))
    
    for digit in range(num_digits+1):
        
        # bucket_sort each digit
        hash_table = {}
        for i, num in enumerate(array):
            digit_val = get_digit(num, digit)
            if hash_table.get(digit_val) is None:
                hash_table[digit_val] = deque([num])
            else:
                hash_table[digit_val].append(num)
        print(hash_table) if to_print else None
        
        # merge each bucket back into original array
        i=0
        for digit in range(0, 10):
            while hash_table.get(digit):
                array[i] = hash_table[digit].popleft()
                i+=1
        print(array) if to_print else None
        
    return array


def qs_partition(array, start, stop, pivot='last', to_print=False):
    """ Pick a pivot (last, first, or random)
    Iterate through the array, Eg. [6, 2, 4, 5, 1, 3]
    If the element is smaller than the pivot:
        swap with the pivot_num, then increment the pivot_idx
    
    =====
    Example 1: pivot='last':
    =====
    
    before: [6, 2, 4, 5, 1, 3] pivot_pos= 5 pivot_num= 3
    0 do nothing, [6, 2, 4, 5, 1, 3] pivot_pos= 5
    1 swap 2 and 6, [6, 2, 4, 5, 1, 3] pivot_pos= 5
    2 do nothing, [2, 6, 4, 5, 1, 3] pivot_pos= 5
    3 do nothing, [2, 6, 4, 5, 1, 3] pivot_pos= 5
    4 swap 1 and 6, [2, 6, 4, 5, 1, 3] pivot_pos= 5
    5 do nothing, [2, 1, 4, 5, 6, 3] pivot_pos= 5
    swap 4 and 3, [2, 1, 4, 5, 6, 3] pivot_pos= 5  # move pivot to pivot_idx
    after: [2, 1, 3, 5, 6, 4] pivot_idx= 2
    
    now quicksort [2, 1] and [5, 6, 4]
    
    
    =====
    Example 2: pivot='first':
    =====
    before: [6, 2, 4, 5, 1, 3, 7] pivot_pos= 0 pivot_num= 6
    0 do nothing, [6, 2, 4, 5, 1, 3, 7] pivot_pos= 0
    1 swap 2 and 6, [6, 2, 4, 5, 1, 3, 7] pivot_pos= 0
    2 swap 4 and 6, [2, 6, 4, 5, 1, 3, 7] pivot_pos= 1
    3 swap 5 and 6, [2, 4, 6, 5, 1, 3, 7] pivot_pos= 2
    4 swap 1 and 6, [2, 4, 5, 6, 1, 3, 7] pivot_pos= 3
    5 swap 3 and 6, [2, 4, 5, 1, 6, 3, 7] pivot_pos= 4
    6 do nothing, [2, 4, 5, 1, 3, 6, 7] pivot_pos= 5
    do nothing, [2, 4, 5, 1, 3, 6, 7] pivot_pos= 5
    after: [2, 4, 5, 1, 3, 6, 7] pivot_idx= 5  # move pivot to pivot_idx

    pivot=6 is now at correct position of pivot_idx=5
    
    now quicksort [2, 4, 5, 1, 3] and [7]
    
    
    =====
    Example 3: pivot='random'
    =====
    
    before: [6, 2, 4, 5, 1, 3] pivot_pos= 3 pivot_num= 5
    0 do nothing, [6, 2, 4, 5, 1, 3] pivot_pos= 3
    1 swap 2 and 6, [6, 2, 4, 5, 1, 3] pivot_pos= 3
    2 swap 4 and 6, [2, 6, 4, 5, 1, 3] pivot_pos= 3
    3 do nothing, [2, 4, 6, 5, 1, 3] pivot_pos= 3
    4 swap 1 and 6, [2, 4, 6, 5, 1, 3] pivot_pos= 3
    5 swap 3 and 5, [2, 4, 1, 5, 6, 3] pivot_pos= 3
    swap 6 and 5, [2, 4, 1, 3, 6, 5] pivot_pos= 5
    after: [2, 4, 1, 3, 5, 6] pivot_idx= 4

    Now quicksort [2, 4, 1, 3]
    
    
    =====
    Example 4: pivot='random'
    =====
    
    Not implemented, move the random pivot to the stop position, then use stop
    See: https://www.geeksforgeeks.org/quicksort-using-random-pivoting/
    """
    pivot_options = {'first': start,
                     'last': stop,
                     'random': random.randrange(start, stop)}  # try some other pivots
    
    pivot_pos = pivot_options[pivot]
    pivot_num = array[pivot_pos]
    
    pivot_idx = start
    print("before:", array[start:stop+1],
          'pivot_pos=', pivot_pos,
          "pivot_num=", pivot_num
         ) if to_print else None
    
    for i, num in enumerate(array[start: stop+1], start):
    
        # skip the pivot
        if i == pivot_pos:
            print(i, 'do nothing,', array, "pivot_pos=", pivot_pos) if to_print else None
            pass
            
        elif num <= pivot_num:
            print(i, f"swap {array[i]} and {array[pivot_idx]},", array,
                  "pivot_pos=", pivot_pos
                 ) if to_print else None
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
            
            # update pivot_pos if it was swapped
            if pivot_idx == pivot_pos:
                pivot_pos = i
            
            pivot_idx += 1
            
        else:
            print(i, 'do nothing,', array, "pivot_pos=", pivot_pos) if to_print else None
            
    # move the pivot to the pivot_idx
    
    if pivot_idx != pivot_pos:
        print(f"swap {array[pivot_idx]} and {array[pivot_pos]},", array,
              "pivot_pos=", pivot_pos
             ) if to_print else None
        array[pivot_idx], array[pivot_pos] = array[pivot_pos], array[pivot_idx]
        
    else:
        print(f"do nothing,", array, "pivot_pos=", pivot_pos) if to_print else None
    
    print("after:", array[start:stop+1], "pivot_idx=", pivot_idx) if to_print else None
    return array, pivot_idx

  
def quick_sort(array, start=0, stop=None, pivot='last', to_print=False): 
    """ Moves the pivot to the pivot_idx
    Numbers <= pivot are moved to the left of the pivot_idx.
    Numbers > pivot are moved to the right of the pivot_idx.
    Recursively sorts left and right subarrays
    """
    if len(array) <= 1:
        return array
    
    if stop==None:
        stop=len(array)-1
    
    if start < stop:
        array, pivot_idx = qs_partition(array, start, stop, pivot, to_print)
        
        array = quick_sort(array, start, pivot_idx-1, pivot, to_print)
        array = quick_sort(array, pivot_idx+1, stop, pivot, to_print)
    return array
