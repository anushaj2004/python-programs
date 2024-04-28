class Node:
    def __init__(self,data):
        self.data = data
        self.next =  None

def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data,end = " ",)
        curr = curr.next
    print()

def insertAtEndOfTail(head,ele):
    newBlock =  Node(ele)
    if head == None:
        return newBlock
    curr = head
    while curr.next!= None:
        curr = curr.next
    curr.next = newBlock
    return head

def deleteHeadNode(head):
    if head == None:
        return None
    SecondNode = head.next
    head.next = None
    return SecondNode

    

n= int(input())
l = map(int,input().split())
head = None
for ele in l:
    head = insertAtEndOfTail(head,ele)
printLinkedList(head)
head = deleteHeadNode(head)
printLinkedList(head)
