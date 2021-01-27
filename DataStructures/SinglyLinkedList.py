# SinglyLinkedList.py 
# Implementation of a singly linked list data structure 

# Defines a class, Node 
class Node:
    # Object constructor for Node 
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def nodePrint(self):
        print("The value of this node is:", self.value)

# Defines a class, LinkedList
class LinkedList:
    # Object constructor for LinkedList
    def __init__(self):
        self.headval = None 

    # Print LinkedList
    def listPrint(self):
        curr = self.headval
        while (curr is not None):
            if curr.next is not None:
                print(curr.value, end = ", ")
            else:
                print(curr.value)
            curr = curr.next

    # Traverses LinkedList to find last node 
    def lastNode(self):
        # Need to assign current so we do not mess up the structure of original linkedList
        current = self.headval
        while current.next is not None: 
            current = current.next
        
        return current

    # Append node to back of linked list 
    def appendNode(self, node):
        last = self.lastNode()
        last.next = node 
        return self

    # Prepend node to start of linked list 
    def prependNode(self, node):
        node.next = self.headval
        self.headval = node
        return self

    # Find target node
    def findNode(self, target):
        current = self.headval
        while current is not None:
            if current.value == target:
                return current

            current = current.next
        
        return current

    # Insert node at index
    def insertNodeIndex(self, index, node):
        if index == 0:
            return self.prependNode(node)

        current = self.headval
        currIndex = 0
        while current.next is not None:
            currIndex += 1
            if currIndex == index:
                 node.next = current.next
                 current.next = node 
                 return self
                
            current = current.next
        
        return self.appendNode(node)

    # Delete target node 
    def removeTargetNode(self, target):
        current = self.headval

        if current.value == target:
            self.headval = current.next
            return self

        while current.next is not None:
            if current.next.value == target:
                current.next = current.next.next 
                return self
            
            current = current.next 
            
        current.next = None

        return self
                
# Creates an empty LinkedList
def createLinkedList():
    return LinkedList()

# Creates a node with value 
def createNode(value):
    return Node(value)

if __name__ == "__main__": 
    newList = createLinkedList()

    for i in range(0,5,2):
        # Create node for each i in range(0,5,2)
        newNode = createNode(i)
        # If newList is empty, headval becomes newNode
        if (newList.headval is None): 
            newList.headval = newNode
        # If newList is not empty, newNode is added to newList
        else:
            # Added to end of newList
            newList.appendNode(newNode)
            # Added to start of newList
            # prependNode(newNode, newList)
            

print("[Original List]:")
newList.listPrint()

print("[Finding node with target value 4]:")
foundNode = newList.findNode(4)
foundNode.nodePrint()

print("[New List after inserting at specified index]:")
addNewNode = createNode(3)
newList.insertNodeIndex(2, addNewNode)
newList.listPrint()

print("[List after removing a node of target value]:")
newList.removeTargetNode(3)
newList.listPrint()


