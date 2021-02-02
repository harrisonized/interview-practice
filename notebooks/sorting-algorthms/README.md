# Questions

##### Iterative

1. Bubble sort: iterate through, swap pairs
2. Selection Sort: iterate through, find minimum, move to front, then repeat
3. Insertion sort: iterate through, compare to previous element, then insert at correct position
4. Counting sort: if you know the range, add the counts to a dictionary, then use that to construct a new list
5. Tree sort: add items to a binary tree, print inorder
6. Heap sort: similar to tree sort, but uses a heap instead

##### Special

1. Bucket sort: if you know the min and max of the array, can split into buckets first, sort each bucket individually
2. Radix sort: each decimal place is a bucket to be sorted, each bucket is sorted using counting sort

##### Recursive

1. Merge sort: Recursively break down the array into halves, then build up again
2. Quick sort: Special case of merge_sort where pivot is chosen randomly instead of in half