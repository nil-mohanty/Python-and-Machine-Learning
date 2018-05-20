n=int(input("Enter the year  "))
if(not n%400):
    print("This is a leap year")
elif(not n%4 and n%100):
    print("This is a leap year")
else:
    print("Not a leap year")
