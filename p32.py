import sys, string, math
n1,k1 = input().split()
n1,k1 = int(n1), int(k1)
L1 = [ int(x1) for x1 in input().split()]
for i in range(0,k1) :
    a1,b1 = input().split()
    a1,b1 = int(a1), int(b1)
    print(sum(L1[a1-1:b1]))
