class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        # To print the list in a readable format
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        # Create the new node
        new_node = Node(value)

        # Case 1: If the list is empty or the new value should be at the head
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            # Case 2: Find the right position to insert
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node

            # Insert the new node at the correct position
            new_node.next_node = current.next_node
            current.next_node = new_node
