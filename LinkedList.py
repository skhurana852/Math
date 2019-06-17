#A Single List list code

class Node:
    # Function to initialize the node
    def __init__(self,data):
        self.data = data    #Assign Data
        self.next = None    #Intialize next as null

#Linked List Class
class LinkedList:

    #Function to intialize the Linked list object
    def __init__(self):
        self.head = None

def printList(headpt):
    i = headpt.head
    while i != None:
        print(i.data)
        i = i.next


if __name__=='__main__':
    # start with empty list
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    #Three Nodes are created
    #Add These nodes in linked list

    llist.head.next = second

    #Add to second
    second.next = third

    print("successfully created")


    #Accessing Linked List Elements

    printList(llist)

    




