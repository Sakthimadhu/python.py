m=input()
e=m.lstrip('-').replace('.','',1).isdigit()
if(e==True):
	print("yes")
else:
	print("No")
