import re
while True:
   regex='^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.w\{2,3})+$'
   mail=input("enter your mail:")
   if(re.search(regex,mail)):
     break
   else:
     print("please enter valid mail id")
     continue
w?hile True:
    pas=input("enter your password:")
    if len(pas)==6 or len(pas)==7 or len(pas)==8:
      break
    else:
      print("not valid")
      continue
while True:
     phnum=input("enter your phone number:")
     if phnum[0]=="9":
       break
     else:
       print("enter valid number")
       continue
def deposite():
       balance=0
       amount=0
       amount=float(input("enter amount"))
       balance+=amount
       print("amount deposited",amount)
def withdrawal():
       balance=0
       amount=0
       amount=float(input("enter amount to be withdrawal"))
       if balance>=amount:
           balance-=amount
           print("you withdrew:",amount)
       else:
           print("insufficient balance")
def avlbalance():
        balance=0
        print("your Available balance is:",balance)
print("enter your choice")
i=int(input("1.Deposite/2.Withdraw/3.Available balance"))
if i==1:
        deposite()
elif i==2:
         withdraw()
elif i==3:
           avlbalance()
else:
         print("please Enter valid number")