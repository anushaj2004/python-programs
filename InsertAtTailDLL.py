class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None 
 
def printLeftToRightManner(head):
    
    curr = head 
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.next 
    print()
 
def printRightToLeftManner(head):
    
    tail = head 
    while tail.next != None:
        tail = tail.next 
        curr = tail
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.prev 
    print()
 
def addNodeAtTailOfLinkedList(head, val):
    newBlock = Node(val)
 
    if head == None:
        return newBlock
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = newBlock 
    newBlock.prev = tail 
    return head

n= int(input())
l = map (int,input().split())
ele= int(input())
head = None
for val in l:
    head = addNodeAtTailOfLinkedList(head, val)
printLeftToRightManner(head)
printRightToLeftManner(head)
head = addNodeAtTailOfLinkedList(head, ele)
printLeftToRightManner(head)
printRightToLeftManner(head)
