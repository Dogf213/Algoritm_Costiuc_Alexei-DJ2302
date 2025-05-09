def test_singly():
    lst = SinglyLinkedList()
    n1 = insert_after_singly(lst, None, 10)
    n2 = insert_after_singly(lst, n1, 20)
    n3 = insert_after_singly(lst, None, 5)
    assert find_singly(lst, 20)[1] == n2
    remove_after_singly(lst, None)  # удалит 5
    assert lst.head.value == 10
    assert_no_cycles_singly(lst)

def test_doubly():
    lst = DoublyLinkedList()
    n1 = insert_after_doubly(lst, None, 10)
    n2 = insert_after_doubly(lst, n1, 20)
    n3 = insert_before_doubly(lst, n1, 5)
    assert find_doubly(lst, 20) == n2
    remove_doubly(lst, n1)
    assert lst.head.value == 5
    assert_no_cycles_doubly(lst)

if __name__ == "__main__":
    test_singly()
    test_doubly()
    print("All tests passed.")
