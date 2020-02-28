import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value > value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif self.value > target:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
         

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
        

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    def print_bft(self,que,node):
        while True:
            if node.left:
                que.enqueue(node)    
            if node.right:
                que.enqueue(node)
            if que.len() == 0:
                break
            else:
                que.dequeue()
        
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        que = Queue()
        self.print_bft(que,node)
       

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def print_dft(self,node_stack,node):
        if node:
            print(node.value)
        if node.left:
            node_stack.push(node)
            self.print_dft(node_stack,node.left)
        if node.right:
            node_stack.push(node)
            self.print_dft(node_stack,node.right)
        if node_stack.len() > 0:
            node_stack.pop()
            
    def dft_print(self, node):
        st = Stack()
        self.print_dft(st,node)
        
    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
