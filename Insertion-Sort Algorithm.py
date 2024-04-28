def insertion_Sort(arr):
    for index in range(1 , len(arr)):
        key = arr[index]
        j =  index - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key 
            
num = int(input())
arr = list(map( int , input().split()))

insertion_Sort(arr)

print(*arr)
