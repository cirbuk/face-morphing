import numpy as np

def doItSmall(a,b):
	x=(a[0]+b[0])//2
	y=(a[1]+b[1])//2
	res=(x,y)
	return res

def doItBig(a,p):
	half=doItSmall(p[a[0]],p[a[1]])
	quad1=doItSmall(p[a[0]],half)
	quad3=doItSmall(half,p[a[1]])
	p.append(half)
	p.append(quad1)
	p.append(quad3)

points=[]
with open("22.txt") as file:
	for line in file:
		x, y=line.split()
		points.append((int(x),int(y)))

theList=[(2,3),(3,4),(5,6),(6,7),(9,10),(12,13),(8,9),(11,12),(1,2),(1,5),(1,8),(1,11)]

for a in theList:
	doItBig(a,points)

out=open("res.txt",'w')
for a in points:
	out.write(str(a[0])+' '+str(a[1])+'\n')
