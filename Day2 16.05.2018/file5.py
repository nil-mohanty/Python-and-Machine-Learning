n1,n2=map(float,input("enter no.s  ").split())
op=input("enter operator A S D M for addn,sub,div and mul ").upper()
if(op=='A'):
    print("sum of %.2f and %.2f is %.2f"%(n1,n2,n1+n2))
elif (op=='S'):
    print("subtraction of %.2f and %.2f is %.2f"%(n1,n2,n1-n2))
elif (op=='M'):
    print("multiplication of %.2f and %.2f is %.2f"%(n1,n2,n1*n2))
elif (op=='D'):
    if(n2!=0.0):
        print("division of %.2f and %.2f is %.2f"%(n1,n2,n1/n2))
    else:
        print("cant divide by zero")
else:
    print("invalid instruction")
