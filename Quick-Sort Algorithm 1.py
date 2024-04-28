def findPivotIndex(nums, left, right):
   
    pivot = nums[right]
    position = left 
 
    # index --> 0 1 2 3 4 5 
    for index in range(left, right):
        if nums[index] < pivot:
            temp = nums[position]
            nums[position] = nums[index]
            nums[index] = temp 
            position += 1 
 
    temp = nums[right]
    nums[right] = nums[position]
    nums[position] = temp 
    return position
 
 
def performQuickSort(nums, left, right):
    
    if left >= right:
        return 
    
    pivotIndex = findPivotIndex(nums, left, right)
    # [10, 15, 17, 20, 100, 90, 18]
    
 
    performQuickSort(nums, left, pivotIndex - 1)
    performQuickSort(nums, pivotIndex + 1, right)
 

n = int(input())
nums = list(map(int,input().split()))



 
performQuickSort(nums, 0, n - 1)
print(*nums)
