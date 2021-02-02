from itertools import islice
from ..custom_errors import EmptyListError, ItemNotFoundError


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """Make sure to only add Node objects to the LinkedList"""
    
    def __init__(self, head=None):
        self.head = head
        self.current = self.head
        
    def get_current(self):
        return self.current.data
        
    def next(self):
        self.current = self.current.next
        return self.current.data
    
    def reset(self):
        self.current = self.head
        return self.head.data
        
    def return_all(self, lim=100):
        curr_node = self.head
        
        i = 0
        while curr_node is not None:
            yield curr_node.data
            curr_node = curr_node.next
            i += 1
            if i == lim:
                break
                
    def print_all(self, lim=100):
        """prints the first 100 items"""
        for item in islice(weekdays.return_all(), 0, 100):
            print(item)
            
    def push(self, new_node):
        """insert node at beginning
        link new_node to first item, then update links"""
        
        if self.head is None:
            self.head = new_node
            return None
        
        new_node.next = self.head
        self.head = new_node
        
    def append(self, new_node):
        """insert node at end
        traverse the list, then add when node.next is none
        """
        
        if self.head is None:
            self.head = new_node
            return None

        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
    
    def insert_node_after_item(self, item, new_node):
        """Traverse the list until item is found
        Update new_node.next to point to curr_node.next
        Update curr_node.next to point to new_node
        """
        curr_node = self.head
        
        while curr_node is not None:
            if curr_node.data == item:
                new_node.next = curr_node.next
                curr_node.next = new_node
                return None
            elif curr_node.data != item and curr_node.next is None:
                raise ItemNotFoundError("please check your input and try again")
            curr_node = curr_node.next
            
    def get_node_at_position(self, n):
        """Traverse the list until position n, n starts at 0, then update links"""
        curr_node = self.head
        
        i = 0
        while i < n:
            if curr_node.next is None:
                raise IndexError("list is shorter than n")
            curr_node = curr_node.next
            i += 1
        
        return curr_node.data
    
    def insert(self, n, new_node):
        """Traverse the list until position n, n starts at 0, then update links"""
        curr_node = self.head
        
        i = 0
        while i < n:
            if curr_node.next is None:
                raise IndexError("list is shorter than n")
            curr_node = curr_node.next
            i += 1
        
        new_node.next = curr_node.next
        curr_node.next = new_node
        
        return None
    
    def remove_head(self):
        self.head = self.head.next
    
    def remove(self, item):
        """Traverse a linked list until item is found
        Need to link previous node to next item
        """
        
        if self.head is None:
            raise EmptyListError
        
        if self.head.data == item:
            self.remove_head()
            return print(f'{item} removed')
        
        prev_node, curr_node = None, self.head  
        
        while curr_node is not None:
            if curr_node.data == item:
                prev_node.next = curr_node.next
                return print(f'{item} removed')
            prev_node = curr_node
            curr_node = curr_node.next
            
        print("item not found")
        
    def remove_all(self):
        self.head = None
    
    def pop(self):
        """remove item from end"""
        prev_node, curr_node = self.head, self.head  # use prev = self.head for single-item list
        
        while curr_node.next is not None:
            prev_node = curr_node
            curr_node = curr_node.next
            
        prev_node.next = None
        return None
    
    def make_circular(self):
        """Make last element link to first"""
        if self.head is None:
            raise EmptyListError("please add items to the list before trying again")
        
        if self.head.next is None:
            self.head.next = self.head
            return None
        
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = self.head
        return None
    
    def reverse(self):
        """
        Example:
        A -> B -> C -> D        
        while at A
        A.next updated to None
        traverse to B
        B.next updated to A
        while at C
        C.next updated to B
        traverse to D
        D.next updated to C
        
        self.head updated to D
        """
        if self.head is None:
            return print("empty list")
        
        if self.head.next is None:
            return print("single item list")
        
        prev_node, curr_node = None, self.head
        
        while curr_node.next is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            
        self.head = curr_node
        self.head.next = prev_node
        
    def get_third_to_last_item(self):
        """
        Example: A -> B -> C -> D
        Return B
        """
        first, second, third = None, None, None
        
        curr_node = self.head
        
        while curr_node is not None:
            first = second
            second = third
            third = curr_node
            curr_node = curr_node.next
        
        if first is not None:
            return first.data
        else:
            raise IndexError("list has fewer than 3 elements")
