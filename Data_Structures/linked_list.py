"""
Linked list methods:
    - Insert at tail
    - Insert list at tail
    - Insert at head
    - Insert list at head
    - New linked list from list
    - Linked list size
    - Print head to tail
    - Print tail to head
    - Reverse linked list

"""

""" Node Class/Structure """
class Node:

    # Constructor
    def __init__(self, value):
        self.val = value
        self.next = None

""" Linked list class """
class Linked_list:

    # constructor
    def __init__(self):
        self.head = None
    

    """ Insert node at tail """
    def insertTail(self, val):

        # Create new node
        newNode = Node(val)

        # insert at head if list is null
        if self.head == None:
            self.head = newNode
            return
        
        # move to tail
        move = self.head

        while move.next != None:
            move = move.next
        
        # append new node
        move.next = newNode


    """ Insert list at tail """
    def insertListTail(self, myList:list):
        
        for val in myList:
            self.insertTail(val)
    
    """ Insert node at head """
    def insertHead(self, val):

        # create new node
        newNode = Node(val)

        # Make new node point to head
        newNode.next = self.head

        # Make new node the new head
        self.head = newNode 
    

    """ Insert list at head """
    def insertListHead(self, myList):

        # loop to insert items
        for val in myList:
            self.insertHead(val)
    

    """ Init liked list from list. Must be an empty list """
    def linkedList_from_list(self, myList):

        # make sure linked list is empty
        if self.head is not None:
            print("\nLinked list must be empty\n")
            

        else:

            addNode = self.head

            for val in myList:
                newNode = Node(val)




    """ Get linked list size """
    def getSize(self) -> int:

        # move variable
        move = self.head

        # counter for nodes
        counter = 0

        # loop to count nodes
        while move.next != None:
            counter+=1
            move = move.next
        
        # return node total
        return counter
    
    
    """ Print head to tail  """
    def printHeadToTail(self):

        # variable to move into list
        move = self.head
        index = 0

        # loop to print nodes
        while move != None:

            # print node val
            print(f"Index {index}: {move.val}\n")
            index += 1
            move = move.next
        
        print("\n")
    

     
    """ Print tail to head """
    def printTailToHead(self):

        # NOTICE: Not optimal solution since reversing list twice

        # reverse list
        self.reverseList()

        # print list when after reverse the list
        self.printHeadToTail()

        # reverse to original order
        self.reverseList()
    

    """ Reverse Linked list """
    def reverseList(self):

        # variables to reassing linkers
        prevNode = None
        currentNode = self.head
        nextNode = Node

        # Loop to reverse linked list
        while currentNode != None:

            # store next node from current node
            nextNode = currentNode.next

            # link current node to prev node (reverse)
            currentNode.next = prevNode

            # make prev node the current node. So, next next node can be linked to this node
            prevNode = currentNode

            # move to next node
            currentNode = nextNode
        
        # make last node the new head 
        self.head = prevNode
            




if __name__ == "__main__":

    myList = Linked_list()

    myList.insertTail(1)
    myList.insertTail(2)
    myList.insertTail(3)

    myList.printHeadToTail()

    myList.reverseList()

    myList.printHeadToTail()

    myList.reverseList()

    myList.insertListTail([4,5,6,7])

    myList.printHeadToTail()

    myList.insertListHead([-2, -1, 0])

    myList.printHeadToTail()

