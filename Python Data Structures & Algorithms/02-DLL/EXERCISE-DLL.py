class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return (self.pop_first())
        elif index == self.length - 1:
            return (self.pop())
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp


# Test Class Constructor

my_doubly_linked_list = DoublyLinkedList(7)

print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length)

"""
    EXPECTED OUTPUT:
    ----------------
    Head: 7
    Tail: 7
    Length: 1

"""


# Test append Method

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)

print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length, '\n')

print('Doubly Linked List:')
my_doubly_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Doubly Linked List:
    1
    2

"""


# Test pop Method

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_doubly_linked_list.pop().value)
# (1) Item -  Returns 1 Node
print(my_doubly_linked_list.pop().value)
# (0) Items - Returns None
print(my_doubly_linked_list.pop())

"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""


# Test prepend Method

my_doubly_linked_list = DoublyLinkedList(2)
my_doubly_linked_list.append(3)

print('Before prepend():')
print('----------------')
print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length, '\n')
print('Doubly Linked List:')
my_doubly_linked_list.print_list()

my_doubly_linked_list.prepend(1)

print('\n\nAfter prepend():')
print('---------------')
print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length, '\n')
print('Doubly Linked List:')
my_doubly_linked_list.print_list()

"""
    EXPECTED OUTPUT:

    Before prepend():
    ----------------
    Head: 2
    Tail: 3
    Length: 2 

    Doubly Linked List:
    2
    3


    After prepend():
    ---------------
    Head: 1
    Tail: 3
    Length: 3 

    Doubly Linked List:
    1
    2
    3

"""


# Test pop_first Method

my_doubly_linked_list = DoublyLinkedList(2)
my_doubly_linked_list.append(1)

# (2) Items - Returns 2 Node
print(my_doubly_linked_list.pop_first().value)
# (1) Item -  Returns 1 Node
print(my_doubly_linked_list.pop_first().value)
# (0) Items - Returns None
print(my_doubly_linked_list.pop_first())

"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""


# Test get method

my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)

print('Get node from first half of DLL:')
print(my_doubly_linked_list.get(1).value)

print('\nGet node from second half of DLL:')
print(my_doubly_linked_list.get(2).value)

"""
    EXPECTED OUTPUT:
    ----------------
    Get node from first half of DLL:
    1

    Get node from second half of DLL:
    2

"""


# Test set Method

my_doubly_linked_list = DoublyLinkedList(11)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(23)
my_doubly_linked_list.append(7)

print('DLL before set_value():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.set_value(1,4)

print('\nDLL after set_value():')
my_doubly_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    DLL before set_value():
    11
    3
    23
    7

    DLL after set_value():
    11
    4
    23
    7

"""


# Test insert Method

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(3)

print('DLL before insert():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.insert(1,2)

print('\nDLL after insert(2) in middle:')
my_doubly_linked_list.print_list()

my_doubly_linked_list.insert(0,0)

print('\nDLL after insert(0) at beginning:')
my_doubly_linked_list.print_list()

my_doubly_linked_list.insert(4,4)

print('\nDLL after insert(4) at end:')
my_doubly_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    DLL before insert():
    1
    3

    DLL after insert(2) in middle:
    1
    2
    3

    DLL after insert(0) at beginning:
    0
    1
    2
    3

    DLL after insert(4) at end:
    0
    1
    2
    3
    4

"""


# Test remove Method

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

print('DLL before remove():')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() in middle:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(0).value)
print('DLL after remove() of first node:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() of last node:')
my_doubly_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    DLL before remove():
    1
    2
    3
    4
    5

    Removed node:
    3
    DLL after remove() in middle:
    1
    2
    4
    5

    Removed node:
    1
    DLL after remove() of first node:
    2
    4
    5

    Removed node:
    5
    DLL after remove() of last node:
    2
    4

"""