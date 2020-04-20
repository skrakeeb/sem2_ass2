import numpy as np 
import matplotlib.pyplot as plt 

x= np.arange(0,1.1,0.1)
h= 0.1
v= np.zeros(11)  # v=y'
y= np.zeros(11)
v[0]=0
y[0]=0
def f1(x1,y1,v1):   #for solving the eqn y'= v
	return(v1)

def f2(x1,y1,v1):   #for solving the eqn y''= f(x,y,y')
	return(2*v1-y1-x1+(x1*np.exp(x1)))

for i in range(10):
	y[i+1]= y[i]+h*f1(x[i],y[i],v[i])
	v[i+1]= v[i]+h*f2(x[i],y[i],v[i])

print(v,'\n',y)	


