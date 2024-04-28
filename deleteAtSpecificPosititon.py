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

def deleteHeadNodeAtSpecificPosition(head,position):
   if position == 1:
       return insertNodeAtHeadOfLinkedList
   curr = head
   index = 1
   while index != position -1:
        curr = curr.next
        index += 1
   mainNode = curr.next
   nextnode = mainNode.next
   mainNode.next = None
   curr.next = None
   curr.next = nextnode
   return head

    

n= int(input())
l = map(int,input().split())
pos = int(input())
head = None
for ele in l:
    head = insertAtEndOfTail(head,ele)
printLinkedList(head)
head = deleteHeadNodeAtSpecificPosition(head,pos)
printLinkedList(head)
