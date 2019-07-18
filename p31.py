n1=int(input())
t=list(map(int,input().split()))
r1=1
l1=[]
for i in t:
  r1=r1*i
for i in t:
  l1.append(r1//i)
print(*l1)
    
