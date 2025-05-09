class SinglyNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

def insert_after_singly(lst, node, value):
    new_node = SinglyNode(value)
    if node is None:
        new_node.next = lst.head
        lst.head = new_node
        if lst.tail is None:
            lst.tail = new_node
    else:
        new_node.next = node.next
        node.next = new_node
        if node == lst.tail:
            lst.tail = new_node
    lst.length += 1
    return new_node

def find_singly(lst, value):
    prev = None
    curr = lst.head
    while curr:
        if curr.value == value:
            return (prev, curr)
        prev = curr
        curr = curr.next
    return (None, None)

def remove_after_singly(lst, node):
    if node is None:
        if lst.head:
            to_remove = lst.head
            lst.head = lst.head.next
            if lst.head is None:
                lst.tail = None
            lst.length -= 1
    else:
        if node.next:
            to_remove = node.next
            node.next = node.next.next
            if to_remove == lst.tail:
                lst.tail = node
            lst.length -= 1

def assert_no_cycles_singly(lst):
    current = lst.head
    count = 0
    while current:
        count += 1
        if count > lst.length:
            raise Exception("Cycle detected in singly linked list!")
        current = current.next
