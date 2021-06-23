while(True):
    a=input("enter C for centigrade or F for fahrenheit:")
    if a=="C":
        c=int(input("enter centigrade:"))
        f=(9/5*c)+32
        print("fehrenheit",f)
    elif a=="F":
        f=int(input("enter fahrenheit:"))
        c=(f-32)*5/9
        print("centigrade",c)
    c=(input("to continue type c:"))
    if c=="c":
        continue
    else:
        print("end")
        break