num = int(input())
l = list(map(int,input().split()))

fix = num - 1
while fix > 0:
    for index in range(fix):
        if l[index] > l[index + 1]:
            l[index], l[index + 1] = l[index + 1],l[index]
    fix -= 1
    
    
print(*l)
