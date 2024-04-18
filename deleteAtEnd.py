class Node:
    def __init__(self,data):
        self.data = data
        self.next =  None

def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data,end = " --> ",)
        curr = curr.next
    print(None)

def insertNodeAtHeadOfLinkedList(head,ele):
    newBlock = Node(ele)
    newBlock.next = head
    return newBlock

def deleteTailNode(head):
    curr = head
    previous = None
    while curr.next != None:
        previous =curr
        curr = curr.next 
    previous.next = None
    return head
    
    

l = [11,22,33,44,55,66,77,88,99,110]
head = None
for ele in l:
    head = insertNodeAtHeadOfLinkedList(head,ele)
printLinkedList(head)
head = deleteTailNode(head)
printLinkedList(head)
head = deleteTailNode(head)
printLinkedList(head)
