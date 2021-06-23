a=[20,31,15,28]
def largest(a):
    m=a[0]
    for i in a:
        if i>m:
            m=i
            
            return m
        b=largest(a)
        print(b)
        
  