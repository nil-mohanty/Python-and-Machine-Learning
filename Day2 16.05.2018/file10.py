list1=input().split()
avg=(int(list1[0])+int(list1[1])+int(list1[2])+int(list1[3])+int(list1[4]))/5

if(avg>=90.0):
    print("Grade A")
elif(avg>=75.0):
    print("Grade B")
elif(avg>=60.0):
    print("Grade C")
elif(avg>=40.0):
    print("Grade D")
else:
    print("Grade F")
