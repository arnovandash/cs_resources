class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start_index, end_index):
        if self.length <= 1:
            return
        
        current = self.head
        prev = None
        i = 0

        # First, find the start position
        while current is not None and i < start_index:
            prev = current
            current = current.next
            i += 1
            
            
        # Markers for the start and end of the section to be reversed
        last_node_before_sublist = prev
        last_node_of_sublist = current

        # Now reverse the nodes within start_index and end_index
        next = None
        while current is not None and i <= end_index:
            next = current.next
            current.next = prev
            prev = current
            current = next
            i += 1
            
        # Connect the reversed sublist back to the list
        if last_node_before_sublist is not None:
            # Connect with the first node of the reversed sublist
            last_node_before_sublist.next = prev
        else:
            # If reversing starts from head, update head to the new first node
            self.head = prev  
        
        # Connect last node of the reversed sublist to the node after the sublist
        last_node_of_sublist.next = current

        return


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""

