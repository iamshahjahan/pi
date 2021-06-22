class Node:
    def __init__(self, val):
        self.next: Node = None
        self.prev: Node = None
        self.val = val

    def __repr__(self):
        return f"{self.val}"


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def addFront(self, val):
        node = Node(val)

        if self.head == None:
            self.head = node
            self.tail = node
            return node

        node.next = self.head
        self.head.prev = node
        self.head = node
        return node

    def remove(self, node: Node):
        #         from front
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            prev = node.prev
            next = node.next

            prev.next = next
            next.prev = prev

    def __repr__(self):
        return f"[({self.head}):({self.tail})]"
