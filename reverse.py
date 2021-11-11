import math 

l=[2,4,5,7,1,3,6,33]
z = len(l)
x= len(l)
y= l[z-1] 
output = [] 
while (z<=x) and (len(output)<len(l)):
        output.append(y)
        z-=1
        y=l[z-1]
print (output)  