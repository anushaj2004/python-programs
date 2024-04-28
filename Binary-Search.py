target = int(input())
num = int(input())
listt = list (map(int,input().split()))
left = 0
right = num - 1
found = False

while left <= right:
    mid = (left + right)//2
    if listt[mid] == target:
        found = True
        break
    elif listt[mid] == True:
        right = mid - 1
    else:
        left = mid + 1
        
if found == True:
    print("Target is present")
else:
    print("Target is not present")
