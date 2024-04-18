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



def insertNodeAtSpecificposition(head,position,value):
    newBlock = Node(value)
    if position == 1:
        newBlock.next = head
        return newBlock
 
    index = 1
    curr = head
    while index != position - 1:
        curr = curr.next
        index += 1

    newBlock.next = curr.next
    curr.next = newBlock
    return head

l = [11,22,33,44,55,66,77,88,99,110]
head = None
for ele in l:
    head = insertNodeAtHeadOfLinkedList(head,ele)
printLinkedList(head)
head = insertNodeAtSpecificposition(head,5,1009)
printLinkedList(head)








