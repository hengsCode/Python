class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.val = value
    
    def printNode(self):
        print("The value of this node is:", self.val)
    
class DLL: 
    def __init__(self):
        self.first = None
        self.last = None 
    
    def printList(self):
        current = self.first 
        while current is not None:
            current.printNode()
            current = current.next
        
def createDLL():
    return DLL()

if __name__ == "__main__":
    newDLL = createDLL()
    