def reconstructQueue(people):
    people = sorted(people, key=lambda x: x[1])
    # print people
    people = sorted(people, key=lambda x: -x[0])
    print people
    res = []
    for p in people:
        res.insert(p[1], p)
    return res

a =[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]   
b = [[10,0], [1,4], [0,0], [1,0], [7,1], [61,2]]   
c = [[2,0], [4,4], [7,1], [3,0], [2,1], [5,10]]   
reconstructQueue(a)
# reconstructQueue(b)
# reconstructQueue(c)
