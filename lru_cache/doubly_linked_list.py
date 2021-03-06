"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, key,value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, key,value):
        current_next = self.next
        self.next = ListNode(key,value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, key,value):
        current_prev = self.prev
        self.prev = ListNode(key,value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, key,value):
        if self.head:
            oldhead = self.head
            oldhead.insert_before(key,value)
            self.head = oldhead.prev
        else:
            self.head = self.tail = ListNode(key,value)
        self.length += 1


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head:
            removehead = self.head
            if self.length > 1:
                self.head = removehead.next
                self.head.prev = None
            else: 
                self.head = self.tail = None
            self.length -=1
            return removehead.value
        else:
            return None
        
    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, key,value):
        if self.tail:
            oldtail = self.tail
            oldtail.insert_after(value)
            self.tail = oldtail.next
        else:
            self.head = self.tail = ListNode(key,value)
        self.length += 1    
        

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail:
            oldtail = self.tail
            if self.length > 1:
                self.tail.next = None
                self.tail = oldtail.prev
            else:
                self.head = self.tail = None
            self.length -=1
            return oldtail.value
        else:
            return None
       

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.key,node.value)
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.key,node.value)
        
        

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.head == node:
            self.remove_from_head()
        elif self.tail == node:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -=1
        
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        max_value = self.head.value
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            node_value = current_node.value
            if (node_value > max_value):
                max_value = node_value
            
        return max_value
