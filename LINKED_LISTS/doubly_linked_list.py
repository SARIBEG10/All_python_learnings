class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList(object):

    def __init__(self):
        self.head = None

    def add(self, data):
        new_data = Node(data)
        new_data.next = self.head
        if self.head is not None:
            self.head.prev = new_data
        self.head = new_data

    def printing(self, node):
        while node is not None:
            print(node.data)
            node = node.next

    def insertion(self, node, value):
        new = Node(value)
        new.next = node.next
        node.next = new
        new.prev = node
        if new.next is not None:
            new.next.prev = new

    def appending(self, value):
        new = Node(value)
        new.next = None
        if self.head is None:
            new.prev = None
            self.head = new
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = new
        new.prev = lastNode

    def delNode(self, node):
        if node.next is None:
            self.x = node.prev
        else:
            node.prev.next = node.next

        if node.prev is None:
            self.y = node.next
        else:
            node.next.prev = node.prev


if __name__ == "__main__":
    x = LinkedList()
    x.add('Saribeg')
    x.add('alenoush')
    x.insertion(x.head, 20)
    x.appending('Barev')
    x.delNode(x.head.next)
    x.printing(x.head)