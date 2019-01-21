def remove_ele(nums, val):
    start = 0
    end = len(nums)-1

    while start < end:
        if nums[start] != val:
            start +=1
        if nums[end] == val:
            end -=1
        if nums[start] == val and nums[end] != val:
            nums[start],nums[end] = nums[end], nums[start]
            start +=1
            end -=1
    print nums
    return start+1

print remove_ele([0,1,2,2,3,0,4,2], 2)