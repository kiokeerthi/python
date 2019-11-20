print ("calc")
calc=int(input("enter the value(1-6): "))
if calc==1:
    k=int(input())
    l=int(input())
    m=k+l
    print("add= ",m)  
elif calc==2:
    k=int(input())
    l=int(input())
    m=k-l
    print("sub= ",m)  
elif calc==3:
    k=int(input())
    l=int(input())
    m=k*l
    print("mul= ",m) 
elif calc==4:
    k=int(input()) 
    l=int(input())
    m=k/l
    print("div= ",m)
elif calc==5:
    k=int(input())
    l=int(input())
    m=k**l
    print("exp= ",m) 
elif calc==6:
    k=int(input())
    l=int(input())
    m=k%l
    print("mod= ",m)