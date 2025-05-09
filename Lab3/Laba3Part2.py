class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def insert_after_doubly(lst, node, value):
    new_node = DoublyNode(value)
    if node is None:
        new_node.next = lst.head
        if lst.head:
            lst.head.prev = new_node
        lst.head = new_node
        if lst.tail is None:
            lst.tail = new_node
    else:
        new_node.next = node.next
        new_node.prev = node
        if node.next:
            node.next.prev = new_node
        node.next = new_node
        if lst.tail == node:
            lst.tail = new_node
    return new_node

def insert_before_doubly(lst, node, value):
    new_node = DoublyNode(value)
    if node is None:
        new_node.prev = lst.tail
        if lst.tail:
            lst.tail.next = new_node
        lst.tail = new_node
        if lst.head is None:
            lst.head = new_node
    else:
        new_node.prev = node.prev
        new_node.next = node
        if node.prev:
            node.prev.next = new_node
        else:
            lst.head = new_node
        node.prev = new_node
    return new_node

def find_doubly(lst, value):
    curr = lst.head
    while curr:
        if curr.value == value:
            return curr
        curr = curr.next
    return None

def remove_doubly(lst, node):
    if node is None:
        return
    if node.prev:
        node.prev.next = node.next
    else:
        lst.head = node.next
    if node.next:
        node.next.prev = node.prev
    else:
        lst.tail = node.prev

def assert_no_cycles_doubly(lst):
    visited = set()
    curr = lst.head
    while curr:
        if id(curr) in visited:
            raise Exception("Cycle detected in doubly linked list!")
        visited.add(id(curr))
        curr = curr.next
