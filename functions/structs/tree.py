from collections import defaultdict, deque
from ..custom_errors import MethodNotFoundError, ItemNotFoundError
from ..formatting.list_tools import peek

# Functions
# # balanced_root_from_sorted_array
# # balanced_tree_from_sorted_array
# # binary_tree_from_array
# # binary_heap_from_array
# # binary_search_intervals
# # bucketer

# Classes
# # Node
# # BinaryTree
# # BinaryHeap


def balanced_root_from_sorted_array(array):
    """Returns the root of a tree constructed from a sorted array
    Recursively and manually set the links
    
    Example 1:
    [1, 2, 3, 4, 5, 6, 7]
    
           4
        /     \
       2       6
     /  \     /  \
    1    3   5    7
    """
    length = len(array)
    
    if length == 0:
        return None
    
    mid = int(length/2)
    
    node = Node(array[mid])
    node.left = balanced_root_from_sorted_array(array[:mid])
    node.right = balanced_root_from_sorted_array(array[mid+1:])

    return node


def balanced_tree_from_sorted_array(array):
    """Uses the root node to create the binary tree
    """
    node = balanced_root_from_sorted_array(array)
    return BinaryTree(node)


def binary_tree_from_array(array):
    tree = BinaryTree(Node(array[0]))
    for item in array[1:]:
        tree.insert(Node(item))
    return tree


def binary_heap_from_array(array):
    heap = BinaryHeap(Node(array[0]))
    for item in array[1:]:
        heap.insert(Node(item))
    return heap


def binary_search_intervals(node, data):
    """Search a binary tree of intervals
    Use with create_intervals and balanced_tree_from_sorted_array

    Example:
           [5.0, 7.5]
          /          \
     [2.5, 5.0]  [7.5, 10.0]
        /
    [0, 2.5]
    """
        
    if data < node.data[0]:
        if node.left:
            node = binary_search_intervals(node.left, data)
        else:
            raise ItemNotFoundError(f"{data} smaller than smallest interval {node.data}.")
    elif data >= node.data[1]:
        if node.right:
            node = binary_search_intervals(node.right, data)
        else:
            raise ItemNotFoundError(f"{data} greater than greatest interval {node.data}.")
        
    return node


def bucketer(array, intervals):
    """Sorts a list into a list of lists based on intervals, remainders are dropped
    Use with create_intervals
    
    Example:
    bucketer([64, 34, 25, 12, 22, 11, 90], [(0, 25.0), (25.0, 50.0), (50.0, 75.0), (75.0, 100.0)])
    [[12, 22, 11], [34, 25], [64], [90]]
    """

    num_intervals = len(intervals) 
    interval_to_idx = defaultdict(dict)
    for idx, interval in enumerate(intervals):
        interval_to_idx[interval] = idx    
    
    tree = balanced_tree_from_sorted_array(intervals)
    
    # using buckets = [[]] * num_intervals causes an error
    buckets = []
    for bucket in range(num_intervals):
        buckets.append([])
    
    for num in array:
        try:
            interval = binary_search_intervals(tree.root, num).data
            buckets[interval_to_idx[interval]].append(num)
        except ItemNotFoundError:
            pass  # drop remainders

    return buckets


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """Make sure to only add Node objects to the Binary Tree
    
    Example 1: Using insert only
    source: https://www.tutorialspoint.com/python_data_structure/python_tree_traversal_algorithms.htm
           27
         /    \
       14      35
      /  \    /  \
    10   19  31  42
    
    tree = BinaryTree(Node(27))
    tree.insert(Node(14))
    tree.insert(Node(35))
    tree.insert(Node(10))
    tree.insert(Node(19))
    tree.insert(Node(31))
    tree.insert(Node(42))
    
    Example 2: Impossible with insert only
    source: https://www.section.io/engineering-education/binary-tree-data-structure-python/

           10
         /    \
       34      89
      /  \    /  \
    20   45  56  54
    
    tree = BinaryTree(Node(10))
    tree.root.left = Node(34)
    tree.root.right = Node(89)
    tree.root.left.left = Node(20)
    tree.root.left.right = Node(45)
    tree.root.right.left = Node(56)
    tree.root.right.right = Node(54)
    """
    
    def __init__(self, root=None):
        self.root = root
        self.current = self.root
    
    def get_current(self):
        return self.current.data
    
    def move_left(self):
        self.current = self.current.left
        return self.current.data
    
    def move_right(self):
        self.current = self.current.right
        return self.current.data
    
    def reset(self):
        self.current = self.root
        return self.root.data
        
    def __insert(self, node, new_node):
        """Traverse down the tree, insert at first open position
        Inserts in level order
        This is breadth first, all the tree traversals are depth first
        """
        
        if new_node.data < node.data:
            if node.left is None:
                node.left = new_node
            else:
                self.__insert(node.left, new_node)

        elif new_node.data > node.data:
            if node.right is None:
                node.right = new_node
            else:
                self.__insert(node.right, new_node)
            
    def insert(self, new_node):
        """level order insert
        """
        if self.root.data is None:
            self.root = new_node
        else:
            self.__insert(self.root, new_node)
           
    def count_leaf_nodes(self, node='default'):
        """recursive count
        """
        if node=='default':
            node = self.root
        
        if node is None:
            return 0
        if(node.left is None and node.right is None):
            return 1
        else: 
            return self.count_leaf_nodes(node.left) + self.count_leaf_nodes(node.right)
            
    def iterative_levelorder(self, node='default'):
        """traverse iteratively
        add current level elements to stack and pop them to return
        """
        
        stack = deque()
        stack.append(self.root)

        while stack:
            node = stack.popleft()
            yield node

            if node.left is not None:
                stack.append(node.left)

            if node.right is not None:
                stack.append(node.right)
    
    def recursive_inorder(self, node='default'):
        """traverse recursively
        left -> root -> right
        """
        
        if node=='default':
            node = self.root

        if node.left:
            yield from self.recursive_inorder(node.left)
            
        yield node
        
        if node.right:
            yield from self.recursive_inorder(node.right)

    def recursive_rev_inorder(self, node='default'):
        """traverse recursively
        right -> root -> left
        """
        
        if node=='default':
            node = self.root
        
        if node.right:
            yield from self.recursive_rev_inorder(node.right)
            
        yield node
        
        if node.left:
            yield from self.recursive_rev_inorder(node.left)
            
    def recursive_postorder(self, node='default'):
        """traverse recursively
        left -> right -> root
        """
        
        if node=='default':
            node = self.root
        
        if node.left:
            yield from self.recursive_postorder(node.left)
        
        if node.right:
            yield from self.recursive_postorder(node.right)
            
        yield node
        
    def recursive_preorder(self, node='default'):
        """traverse recursively
        root -> left -> right
        """

        if node=='default':
            node = self.root
            
        yield node
        
        if node.left:
            yield from self.recursive_preorder(node.left)
        
        if node.right:
            yield from self.recursive_preorder(node.right)
    
    def iterative_inorder(self, node='default'):
        """See: https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
        
        1) Create an empty stack.
        2) Initialize current node as root
        3) Push the current node to S and set current = current->left until current is NULL
        4) If current is NULL and stack is not empty then 
             a) Pop the top item from stack.
             b) Print the popped item, set current = popped_item->right 
             c) Go to step 3.
        5) If current is NULL and stack is empty then we are done.
        
        Example 1:
        add 27, add 14, add 10, pop 10, return 10, node.right=None
        pop 14, return 14, node.right=19
        add 19, pop 19, return 19, node.right=None
        pop 27, return 27, node.right=35
        add 35, add 31, pop 31, return 31, node.right=None
        pop 35, return 35, node.right=42
        add 42, pop 42, return 42, node.right=None
        """
        
        if node=='default':
            node = self.root
            
        stack = deque()
        
        while True:
            # during first loop, adds all left nodes to stack
            # during subsequent loops, may add if node.right exists
            while node is not None:
                stack.append(node)
                node = node.left
            
            if stack:
                node = stack.pop()
                yield node
                node = node.right  # adds node.right to stack if it exists
                
            else:
                break
    
    def iterative_preorder(self, node='default'):
        
        if node=='default':
            node = self.root
            
        stack = deque()
        stack.append(node)
        
        while stack:
            node = stack.pop()
            yield node
            
            if node.right:
                stack.append(node.right)
                
            if node.left:
                stack.append(node.left)
        
    def iterative_postorder(self, node='default'):
        
        if node=='default':
            node = self.root
            
        stack = deque()
        
        while True:
            while node:
                if node.right is not None: 
                    stack.append(node.right)
                    
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            
            if node.right is not None and peek(stack) == node.right:
                stack.pop()
                stack.append(node)
                node = node.right
                
            else:
                yield node
                node = None
                
            if not stack:
                break            
            
    def print_tree(self, method='recursive', order='inorder'):
        """Valid options:
        order: ['inorder', 'preorder', 'postorder']
        method: ['recursive', 'iterative']
        """
        
        traverse = {'recursive': {'inorder': self.recursive_inorder(),
                                  'preorder': self.recursive_preorder(),
                                  'postorder': self.recursive_postorder(),},
                    'iterative': {'inorder': self.iterative_inorder(),
                                  'preorder': self.iterative_preorder(),
                                  'postorder': self.iterative_postorder(),
                                  'levelorder': self.iterative_levelorder(),}}
        
        if traverse.get(method, {}).get(order) is None:
            raise MethodNotFoundError(f"Please check your inputs: order='{order}', method='{method}'")

        for node in traverse[method][order]:
            print(node.data)
            
    def print_leaf_nodes(self, order='left_to_right'):
        if order=='left_to_right':
            for node in self.recursive_inorder():
                if (node.left is None and node.right is None):
                    print(node.data)
                    
        elif order=='right_to_left':
            for node in self.recursive_rev_inorder():
                if (node.left is None and node.right is None):
                    print(node.data)
                    
        else:
            raise MethodNotFoundError(f"Please check your input: order='{order}'")
        
    def search(self, data, order='levelorder'):
        """ iterative search, this is bad for binary search trees """
        
        traverse = {'levelorder': self.iterative_levelorder(),
                    'inorder': self.recursive_inorder(),
                    'preorder': self.recursive_preorder(),
                    'postorder': self.recursive_postorder()}
        
        if traverse.get(order) is None:
            raise MethodNotFoundError(f"Please check your inputs: method='{method}'")
        
        for node in traverse[order]:
            if node.data == data:
                return node

        return print("Not found")

    def binary_search(self, data):
        """ """

        return node


class BinaryHeap:
    """Make sure to only add Node objects to the Binary Heap
    
    Example 1: Using insert only
    source: https://www.tutorialspoint.com/python_data_structure/python_tree_traversal_algorithms.htm
            2
         /    \
       10      9
      /  \    /
     5    6  1
    
    heap = BinaryHeap(Node(2))
    heap.insert(Node(10))
    heap.insert(Node(9))
    heap.insert(Node(5))
    heap.insert(Node(6))
    heap.insert(Node(1))
    """
    
    def __init__(self, root=None):
        self.root = root
            
    def find_parent(self, curr_node):
        for parent_node in self.iterative_inorder():
            if (parent_node.left == curr_node) or parent_node.right == curr_node:
                return parent_node
        
    def swap(self, curr_node, child_node):
        """swap links on curr and child nodes
        update root if swap
        """
        if curr_node == self.root:
            self.root = child_node
        
        if curr_node.left == child_node:
            curr_node.right, child_node.right = child_node.right, curr_node.right
            curr_node.left, child_node.left = child_node.left, curr_node
            
        elif curr_node.right == child_node:
            curr_node.left, child_node.left = child_node.left, curr_node.left
            curr_node.right, child_node.right = child_node.right, curr_node

    def heapsort(self):
        """Only swaps one-layer deep
        Traverses from bottom up in postorder
        
        In the future: try to recurse down and place the new node at the right spot
        For now, can just keep rerunning this, it will eventually sort itself
        """
        
        for curr_node in self.recursive_postorder():
            try:
                print(curr_node.data, prev_node.data)
            except:
                print(curr_node.data, None)
            
            max_node = max([node for node in [curr_node, curr_node.left, curr_node.right] if node is not None],
                           key=attrgetter("data"))
            
            if max_node == curr_node.left:
                
                parent_node = self.find_parent(curr_node)
                if parent_node:
                    if parent_node.left == curr_node:
                        parent_node.left = curr_node.left
                    elif parent_node.right == curr_node:
                        parent_node.right = curr_node.left

                print('swap left', curr_node.data, curr_node.left.data)
                self.swap(curr_node, curr_node.left)
                    
            elif max_node == curr_node.right:
                
                parent_node = self.find_parent(curr_node)
                if parent_node:
                    if parent_node.left == curr_node:
                        parent_node.left = curr_node.right
                    elif parent_node.right == curr_node:
                        parent_node.right = curr_node.right

                print('swap right', curr_node.data, curr_node.right.data)
                self.swap(curr_node, curr_node.right)

            else:
                pass
                    
            prev_node = curr_node            
                    

    def insert(self, new_node):
        """level order insert
        See: https://www.geeksforgeeks.org/insertion-in-a-binary-tree-in-level-order/
        """
        if self.root is None:
            self.root = new_node
        
        for node in self.iterative_levelorder():
            if not node.left:
                node.left = new_node
                break

            if not node.right:
                node.right = new_node
                break
            
    def recursive_inorder(self, node='default'):
        """traverse recursively
        left -> root -> right
        """
        
        if node=='default':
            node = self.root

        if node.left:
            yield from self.recursive_inorder(node.left)
            
        yield node
        
        if node.right:
            yield from self.recursive_inorder(node.right)
            
    def recursive_postorder(self, node='default'):
        """traverse recursively
        left -> right -> root
        """
        
        if node=='default':
            node = self.root
        
        if node.left:
            yield from self.recursive_postorder(node.left)
        
        if node.right:
            yield from self.recursive_postorder(node.right)
            
        yield node
        
    def iterative_levelorder(self, node='default'):
        """traverse iteratively
        add current level elements to stack and pop them to return
        """
        
        stack = deque()
        stack.append(self.root)

        while stack:
            node = stack.popleft()
            yield node

            if node.left is not None:
                stack.append(node.left)

            if node.right is not None:
                stack.append(node.right)
                
    def iterative_inorder(self, node='default'):
        """See: https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
        
        1) Create an empty stack.
        2) Initialize current node as root
        3) Push the current node to S and set current = current->left until current is NULL
        4) If current is NULL and stack is not empty then 
             a) Pop the top item from stack.
             b) Print the popped item, set current = popped_item->right 
             c) Go to step 3.
        5) If current is NULL and stack is empty then we are done.
        
        Example 1:
        add 27, add 14, add 10, pop 10, return 10, node.right=None
        pop 14, return 14, node.right=19
        add 19, pop 19, return 19, node.right=None
        pop 27, return 27, node.right=35
        add 35, add 31, pop 31, return 31, node.right=None
        pop 35, return 35, node.right=42
        add 42, pop 42, return 42, node.right=None
        """
        
        if node=='default':
            node = self.root
            
        stack = deque()
        
        while True:
            # during first loop, adds all left nodes to stack
            # during subsequent loops, may add if node.right exists
            while node is not None:
                stack.append(node)
                node = node.left
            
            if stack:
                node = stack.pop()
                yield node
                node = node.right  # adds node.right to stack if it exists
                
            else:
                break

    def print_tree(self, order='inorder'):
        i = 0
        if order == 'inorder':
            
            for node in self.recursive_inorder():
                print(node.data)
                i += 1
                if i == 100:
                    break
                
        if order == 'levelorder':
            for node in self.iterative_levelorder():
                print(node.data)
                i += 1
                if i == 100:
                    break
                