s,k=input().split()
k=int(k)
s=str(s)
for i in range (0,len(s),k):
  print(s[i:i+k],end=" ")
