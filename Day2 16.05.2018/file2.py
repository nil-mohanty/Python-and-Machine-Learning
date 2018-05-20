sp,cp=map(float,input("enter the sp and cp\n").split())
if sp>cp:
    print("Profit made is INR"+str((sp-cp)))
elif sp<cp:
    print("Loss occured is INR"+str((cp-sp)))
else:
    print("No profit or loss made")
