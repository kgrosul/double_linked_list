import double_linked_list
import random


def double_linked_list_to_list(my_list):
    result = []
    current_item = my_list.first()
    while current_item != my_list.last().next_item:
        result += [current_item.element]
        current_item = current_item.next_item
    return result


def test_push():
    test_list = double_linked_list.DoubleLinkedList()
    ordinary_list = []
    for i in range(1000):
        a = random.randint(-1000, 1000)
        test_list.push(a)
        ordinary_list += [a]

    assert double_linked_list_to_list(test_list) == ordinary_list


def test_unshift():
    test_list = double_linked_list.DoubleLinkedList()
    ordinary_list = []
    for i in range(1000):
        a = random.randint(-1000, 1000)
        test_list.unshift(a)
        ordinary_list = [a] + ordinary_list

    assert double_linked_list_to_list(test_list) == ordinary_list


def test_pop():
    test_list = double_linked_list.DoubleLinkedList()
    ordinary_list = []
    for i in range(1000):
        a = random.randint(-1000, 1000)
        test_list.push(a)
        ordinary_list += [a]

    for i in range(random.randint(0, 1000)):
        test_list.pop()
        ordinary_list = ordinary_list[:-1]

    assert double_linked_list_to_list(test_list) == ordinary_list


def test_shift():
    test_list = double_linked_list.DoubleLinkedList()
    ordinary_list = []
    for i in range(1000):
        a = random.randint(-1000, 1000)
        test_list.push(a)
        ordinary_list += [a]

    for i in range(random.randint(0, 1000)):
        test_list.shift()
        ordinary_list = ordinary_list[1:]

    assert double_linked_list_to_list(test_list) == ordinary_list


def test_first():
    test_list = double_linked_list.DoubleLinkedList()
    ordinary_list = []
    for i in range(1000):
        a = random.randint(-1000, 1000)
        test_list.push(a)
        ordinary_list += [a]

    for i in range(random.randint(0, 999)):
        test_list.shift()
        ordinary_list = ordinary_list[1:]

    assert test_list.first().element == ordinary_list[0]


def test_last():
    test_list = double_linked_list.DoubleLinkedList()
    ordinary_list = []
    for i in range(1000):
        a = random.randint(-1000, 1000)
        test_list.push(a)
        ordinary_list += [a]

    for i in range(random.randint(0, 999)):
        test_list.shift()
        ordinary_list = ordinary_list[1:]

    assert test_list.last().element == ordinary_list[-1]


def test_len():
    test_list = double_linked_list.DoubleLinkedList()
    ordinary_list = []
    for i in range(1000):
        a = random.randint(-1000, 1000)
        test_list.push(a)
        ordinary_list += [a]

    for i in range(random.randint(0, 999)):
        test_list.shift()
        ordinary_list = ordinary_list[1:]

    assert len(test_list) == len(ordinary_list)


def test_contains():
    test_list = double_linked_list.DoubleLinkedList()
    ordinary_list = []
    for i in range(1000):
        a = random.randint(-1000, 1000)
        test_list.push(a)
        ordinary_list += [a]

    for i in range(random.randint(0, 1000)):
        test_list.shift()
        ordinary_list = ordinary_list[1:]

    for i in range(1000):
        a = random.randint(-1000, 1000)
        if (a in test_list) != (a in ordinary_list):
            assert False
    assert True


def test_delete():
    test_list = double_linked_list.DoubleLinkedList()
    ordinary_list = []
    for i in range(1000):
        a = random.randint(-1000, 1000)
        test_list.push(a)
        ordinary_list += [a]

    for i in range(random.randint(0, 1000)):
        test_list.shift()
        ordinary_list = ordinary_list[1:]

    for i in range(random.randint(0, 1000)):
        a = random.randint(-1000, 1000)
        while a in ordinary_list:
            ordinary_list.remove(a)

        test_list.delete(a)

    assert double_linked_list_to_list(test_list) == ordinary_list


def test_zero_len():
    test_list = double_linked_list.DoubleLinkedList()
    assert len(test_list) == 0


def test_zero_push_pop():
    test_list = double_linked_list.DoubleLinkedList()
    test_list.push(1)
    test_list.pop()
    assert len(test_list) == 0


def test_zero_unshift_shift():
    test_list = double_linked_list.DoubleLinkedList()
    test_list.unshift(1)
    test_list.shift()
    assert len(test_list) == 0


def test_zero_delete():
    test_list = double_linked_list.DoubleLinkedList()
    test_list.unshift(1)
    test_list.pop()
    assert len(test_list) == 0
