Q = []
n = int(input().strip())
while n > 0:
    llist = list(map(int, input().split()))
    l = llist[0]
    if l == 1:
        num = llist[1]
        Q.append(num)
        print(num, "inserted")
    elif l == 2:
        if len(Q) == 0:
            print("Queue is empty")
        else:
            print(Q[0])
    elif l == 3:
        if len(Q) == 0:
            print("Queue is empty")
        else:
            print(Q[0])
            Q.pop(0)
    elif l == 4:
        if len(Q) == 0:
            print("Queue is empty")
        else:
            for ele in Q:
                print(ele, end = " ")
            print()
    else:
        if len(Q) == 0:
            print("Queue is empty")
        else:
            print("Queue is not empty")
       
    n -= 1
