import numpy as np

x=open('21.jpg.txt','r')
y=open('22.jpg.txt','r')
z=open('res.txt','w')

a=np.zeros((132,2))
i=0
for line in x:
	x1,x2=line.split()
	a[i][0]+=int(x1)
	a[i][1]+=int(x2)
	i=i+1

i=0
for line in y:
	y1,y2=line.split()
	a[i][0]+=int(y1)
	a[i][1]+=int(y2)
	i=i+1

for i in range(0,132):
	z.write(str(int(a[i][0]//2))+' '+str(int(a[i][1]//2))+'\n')

x.close()
y.close()
z.close()