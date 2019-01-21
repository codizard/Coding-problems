a = [1,2,3]
b =  str(a) + "->" + str(a)
i, p = b.split("->")[0], b.split("->")[1]
print i.split(",")
print p