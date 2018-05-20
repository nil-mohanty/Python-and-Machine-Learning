n=input("enter 8length binary number")
c=0
"""if(len(n)==8):
    if(n[0]==1):
        print("Even parity")
    else:
        print("Odd Parity")
elif(len(n)<8):
    print("Odd parity")
else:
    print("Give a 8length binary number not more")"""
if(len(n)==8):
    if(n[0]=='1'):
        c=c+1
    if(n[1]=='1'):
        c=c+1
    if(n[2]=='1'):
        c=c+1
    if(n[3]=='1'):
        c=c+1
    if(n[4]=='1'):
        c=c+1
    if(n[5]=='1'):
        c=c+1
    if(n[6]=='1'):
        c=c+1
    if(n[7]=='1'):
        c=c+1
    if(c%2==0):
        print("even parity")
    else:
        print("odd parity")
else:
    print("give exactly 8 digits")


