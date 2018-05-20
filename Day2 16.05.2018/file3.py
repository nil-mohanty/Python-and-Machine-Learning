p,t,r,n=map(float,input("enter the principal time rate compounding year\n").split())
print("Simple interest gained is %0.2f INR"%(p*t*r/100))
print("Compound interest gained is %0.2f INR"%((p*((1+(r*0.01/n))**(n*t)))-p))

