import sys, string, math
s11 = input()
s22= input()
s33 = string.ascii_lowercase
L1 = []
for i in range(0, len(s11)) :
    k1 = ord(s11[i]) + s33.index(s22[i]) + 1
    if k1 > ord('a')+25 :
        k1 -= 26
    #print(k1,chr(k1))
    L1.append(chr(k1))
s44 = ''.join(L1)
print(s44)


