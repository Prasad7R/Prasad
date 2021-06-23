import copy
l1=[1,2,[3,4],5]
l2=copy.deepcopy(l1)
print(l1)
print(l2)
l2[2][0]='a'
print(l1)
print(l2)

