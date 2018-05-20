n=input("enter the number ")
if(not len(n)%2):
    print("try an odd length digit\n")
else:
    m=input("enter  digit ")
    if(len(m)==1):
        if(n[(len(n)//2)]==m):
            print("Matched")
        else:
            print("Not matched")
    else:
        print("Checking digit should be a single digit.")
