class Item:
    def __init__(self, element, next_item=None, prev_item=None):
        self.element = element
        self.next_item = next_item
        self.prev_item = prev_item


class DoubleLinkedList:
    def __init__(self):
        self.__head = Item(None)
        self.__tail = Item(None)
        self.__head.next_item = self.__tail
        self.__tail.prev_item = self.__head

    def push(self, element):
        new_item = Item(element)
        new_item.prev_item = self.__tail.prev_item
        self.__tail.prev_item.next_item = new_item
        self.__tail.prev_item = new_item
        new_item.next_item = self.__tail

    def pop(self):
        assert self.__len__() != 0
        self.__tail.prev_item.prev_item.next_item = self.__tail
        self.__tail.prev_item = self.__tail.prev_item.prev_item

    def unshift(self, element):
        new_item = Item(element)
        new_item.next_item = self.__head.next_item
        self.__head.next_item.prev_item = new_item
        self.__head.next_item = new_item
        new_item.prev_item = self.__head

    def shift(self):
        assert self.__len__() != 0
        self.__head.next_item.next_item.prev_item = self.__head
        self.__head.next_item = self.__head.next_item.next_item

    def __delete(self, item):
        prev_item = item.prev_item
        next_item = item.next_item
        prev_item.next_item = next_item
        next_item.prev_item = prev_item

    def first(self):
        assert self.__head != self.__tail
        return self.__head.next_item

    def last(self):
        assert self.__head != self.__tail
        return self.__tail.prev_item

    def delete(self, element):
        current_item = self.first()

        while current_item != self.__tail:
            new_item = current_item.next_item
            if current_item.element == element:
                self.__delete(current_item)

            current_item = new_item

    def __len__(self):
        counter = 0
        current_item = self.__head
        while current_item.next_item != self.__tail:
            counter += 1
            current_item = current_item.next_item
        return counter

    def __contains__(self, element):
        current_item = self.__head.next_item
        while current_item != self.__tail:
            if current_item.element == element:
                return True
            current_item = current_item.next_item
        return False
