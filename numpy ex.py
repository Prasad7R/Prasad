import numpy as n

a=n.array([[1,3,4],[6,7,4],[7,5,2]])

#b=n.array([[1,3,4],[6,7,4],[7,5,2]])
#print (n.dot(a,b))
#b=(a.ravel())
#print(b)
#print(a.ndim)
#print(b.ndim)

#b.shape=(3,3)
#print(b.ndim)

b=a.tranpose()
print(b)