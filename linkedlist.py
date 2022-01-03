class Node:
    def __init__ (self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__ (self):
        self.head=None
    
    def reverse(self):
        prev=None
        current=self.head
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev

    def push(self, newData):
        newNode=Node(newData)
        newNode.next=self.head
        self.head=newNode

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

list=LinkedList()
list.push(34)
list.push(545)
list.push(3)
list.push(9)
list.push(45)

list.printList()
list.reverse()
list.printList()