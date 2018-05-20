n=float(input("enter units used \n"))
total=0
if(n<=50.0):
    total=n*0.5
elif(n<=100.0):
    total=((n-50.0)*0.75)+25
elif(n<=200):
    total=25+37.5+(n-100)
else:
    total=25+37.5+100+((n-200)*1.8)
    
print("total bill is %0.2f"%total)