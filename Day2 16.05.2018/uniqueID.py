name=[]
accl=['0','1','3','4','5']
spl=[')','!','@','#','$','%','^','&','*','(']
name=input("enter your full name with spaces in between\n").upper().split()
if(len(name)!=0):
    mob=input("enter 10 digit mobile number\n")
    if(len(mob)==10):
        pin=input("enter your 6 digit pin code\n")
        if(len(pin)==6):
            acc=input("enter the kind of account you want\n 0-Person \n 1-pvtCompany \n 3-NGO\n 4.Government \n 5-Defense\n ")
            if(acc in accl):
                tot=int(mob[0])+int(mob[1])+int(mob[2])+int(mob[3])+int(mob[4])+int(mob[5])+int(mob[6])+int(mob[7])+int(mob[8])+int(mob[9])
                print("1st sum ",tot)
                tot=str(tot)
                tot1=str(int(tot[0])+int(tot[1]))
                print("2nd sum ",tot1)
                if(len(tot1)==2):
                    tot2=str(int(tot1[0])+int(tot1[1]))
                else:
                    tot2=tot1
                print("final sum ",tot2)
                mobl=spl[int(tot2)]
                print("spl is ",mobl)
                if(len(name)==1):
                    account=pin+name[0][0]+name[0][1]+mobl+acc
                else:                
                    account=pin+name[0][0]+name[-1][0]+mobl+acc
                
                print("YOUR ACCOUNT ID IS ",account)
            else:
                print("invalid acc type")
        else:
            print("Invalid ZIP code")
    else:
        print("Invalid mobile number")
else:
    print("name cant be empty")