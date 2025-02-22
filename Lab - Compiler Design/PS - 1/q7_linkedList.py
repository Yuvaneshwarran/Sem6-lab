import json


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data})'


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return self.head
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode

    def display(self):
        node = []
        temp = self.head
        while temp:
            node.append(str(temp.data))
            temp = temp.next
        return " -> ".join(node)


def readJson():
    with open('storeKeywords.json', 'r') as file:
        data = json.load(file)
    return data['keywords']


def array(arr):
    print(arr, "\n")


if __name__ == '__main__':
    keywords = readJson()
    print("Array Representation:")
    array(keywords)

    print("Linked list Representation:")
    cnode = LinkedList()
    for i in keywords:
        cnode.insert(i)

    disp = cnode.display()
    print(disp)

    print()
