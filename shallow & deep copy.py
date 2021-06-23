import copy
l1=[1,3,[5,7],11]

l2=copy.copy(l1)
l3=copy.deepcopy(l1)


print("original list",l1,id(l1))
print("shallow copy",l2,id(l2))
print("deep copy",l3,id(l3))

l1[2][1]=4

print("original list",l1,id(l1))
print("shallow copy",l2,id(l2))
print("deep copy",l3,id(l3))