class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # if list is empty, do nothing
        if self.head is None:
            return None
        # if the node is at the end of the list
        if node.next_node is None:
            # that node is the new head
            self.head = node
            return
        # pass the next node to the reverse method
        self.reverse_list(node.next_node, None)
        # set following to the next node of the current node
        following = node.next_node
        # reverse the link by setting the next node of following to the current node
        following.next_node = node
        # remove the original link
        node.next_node = None
