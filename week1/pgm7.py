n=int(input("enter the year"))
if(n%4==0):
    if(n%100==0):
        if(n%400==0):
            print("true")
        else:
            print("flase")
    else:
        print("true")
else:
    print("flase")     