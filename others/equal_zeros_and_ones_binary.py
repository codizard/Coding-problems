from collections import defaultdict

def largest_subarray(arr):
    
    if arr is None or len(arr) == 0:
        return 0
    
    first_found = defaultdict(int)
    first_found[0] = 0
    count = 0
    largest = 0
    for ind, value in enumerate(arr):
        print first_found
        if value == 1:
            count += 1
        else:
            count -= 1
        
        if count not in first_found:
            first_found[count] = ind + 1
        else:
            print "updated largest"
            largest = max(largest, ind - first_found[count] + 1)
            
    return largest

print largest_subarray([0,0,0,0,1,1])