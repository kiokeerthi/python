n=int(input())
for k in range(n):
  for l in range(k+1):
    print("* ",end=" ")
  print("\r")
for i in range(n,0,-1):
  for j in range(i-1):
    print("* ",end=" ")
  print("\r")