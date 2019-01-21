def nextPermutation(nums):
    if len(nums) == 0:
        return

    #find the first decreasing element
    i = len(nums) -1 
    index = None
    while i > 0:
        if nums[i] > nums[i-1]:
            index = i
            break
        i-=1
    if not index:
        nums.reverse()
        return
    
    #Swap a[i-1] and a[i]
    nums[index-1], nums[index] = nums[index], nums[index-1]
    nums[index:] = list(reversed(nums[index:]))

nums = [3, 4 ,6 ,8, 9, 6, 5]
nextPermutation(nums)
print nums


