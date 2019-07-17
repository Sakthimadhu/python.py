x1=int(input())
guru=list(map(int,input().split()))
ln=[]
for i in guru:
    if guru.count(i)>1:
        if str(i) not in ln:
            ln.append(str(i))
if len(ln)==0:
    print("unique")
else:
    print(" ".join(ln))
