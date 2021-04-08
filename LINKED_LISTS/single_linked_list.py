class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None

    def printing(self):
        printValue = self.head
        while printValue is not None:
            print(printValue.data)
            printValue = printValue.next

    def beg(self, data4):
        new_data = Node(data4)
        new_data.next = self.head
        self.head = new_data

    def end(self, data5):
        end_data = Node(data5)
        if self.head is None:
            self.head = end_data
            return
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = end_data

    def between(self, node, value):
        new_data = Node(value)
        new_data.next = node.next
        node.next = new_data

    def delNode(self, datavalue):
        prev = None
        new = self.head     # injam new object az self.head shoru mishe
        if new is not None:
            if new.data == datavalue:
                self.head = new.next
                return

        while new is not None:
            if new.data == datavalue:
                break   # in tike yadam bashe return nist bayad break bashe
            prev = new
            new = new.next

        if new is None:
            return
        prev.next = new.next


if __name__ == "__main__":
    x = LinkedList()
    x.head = Node('Saribeg')
    data2 = Node('Alenoush')
    data3 = Node('kyanks')
    x.head.next = data2
    data2.next = data3
    x.beg('Alenoush2')
    x.end('barev')
    x.between(x.head, 'Hello')
    x.delNode('kyanks')
    x.printing()