def contains_all(s, arr):
    i, j = 0,0
    array = []
    length = float('inf')
    while i < len(arr) and j < len(arr):
        if s.issubset(arr[i:j+1]):
            print "considering", arr[i:j+1]
            if j-i+1 < length:
                length = j-i+1
                array = arr[i:j+1]
            while arr[i] not in s or arr[i] in set(arr[i+1:j]):
                if arr[i] not in s:
                    i+=1
                else:
                    i+=1
                    if j-i+1 < length:
                        length = j-i+1
                        array = arr[i:j+1]
            i = j
        else:
            j+=1
    return length, array
S = "ADOBECODEBANC"
T = "ABC"
print contains_all(set(T) ,list(S))


# b = set()
# b.add(1)
# b.add(3)
# b.add(2)
# a = []
# a.append(1)
# a.append(4)
# a.append(2)
# a.append(3)

# print set(b).issubset(a)