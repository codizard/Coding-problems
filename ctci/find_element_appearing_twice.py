def find_element_appearing_twice(nums):
    res = []
    for i in range(len(nums)):
        if nums[abs(nums[i])-1] > 0:
            nums[abs(nums[i])-1] *= -1
        else:
            res.append(abs(nums[i]))
    return res

print find_element_appearing_twice([4,3,2,7,8,2,3,1])