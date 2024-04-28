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
        print(curr.data,end =" ")
        curr = curr.prev
    print()






def addNodeAtHeadOfLinkedList(head,val):
    newBlock = Node(val)
    if head == None:
        return newBlock
    newBlock.next = head
    head.prev =  newBlock
    return newBlock



def addNodeAtTail(head,val):
    newBlock = Node(val)
    if head == None:
        return newBlock
    tail = head
    while tail.next != None:
        tail = tail.next
    #left to right link
    #11 -->22 -->33-->44 -->None
    #newBlock = 44
    #tail = 33
    tail.next = newBlock
    #right to left link
    newBlock.prev = tail
    return head



n= int(input())
l = map (int,input().split())
val = int(input())
head = None
for ele in l:
    head = addNodeAtHeadOfLinkedList(head,ele)
printRightToLeftManner(head)
printLeftToRightManner(head)
head = addNodeAtTail(head,val)
printRightToLeftManner(head)
printLeftToRightManner(head)
