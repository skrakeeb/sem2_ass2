'''
coded by: rakeeb 
coded for: implimentation of shooting method with some candidate solutions
'''

import numpy as np 
import matplotlib.pyplot as plt 

t= np.arange(0,10.5,0.5)
h=0.5
x= np.zeros(t.size)
v= np.zeros(t.size)
x_a=0
x_b=0

x[0]= x_a
v[0]= 70   #guess of the initial condition

def f1(t1,x1,v1):   #for solving the eqn x'= v
	return(v1)

def f2(t1,x1,v1):   #for solving the eqn x''= f(t,x,x')
	return(-10)

abs_err=  30

while abs_err >= 20 :
	for i in range(t.size-1):
		k10= h*f1(t[i],x[i],v[i])
		k20= h*f2(t[i],x[i],v[i])

		k11= h*f1((t[i]+ h/2), x[i]+k10/2, v[i]+k20/2)
		k21= h*f2((t[i]+ h/2), x[i]+k10/2, v[i]+k20/2)

		k12= h*f1((t[i]+ h/2), x[i]+k11/2, v[i]+k21/2)
		k22= h*f2((t[i]+ h/2), x[i]+k11/2, v[i]+k21/2)

		k13= h*f1(t[i]+h, x[i]+k12, v[i]+k22)
		k23= h*f2(t[i]+h, x[i]+k12, v[i]+k22)

		x[i+1]= x[i]+(1/6)* (k10+ 2*k11 + 2*k12 + k13)
		v[i+1]= v[i]+(1/6)*  (k20+ 2*k21 + 2*k22 + k23)

	end_val= x[(x.size -1)]	#value of the solution at right boundary point 
	error= (x_b - end_val)  # error from the given boundary condition
	abs_err= abs(error)
	if  error < 0:       #i.e end_val is greater. So we reduce the assumed initial condition 
		v[0]= v[0]*0.8
	else :               # i.e end_val is smaller. So we increase the assumed initial condition 
		v[0]=v[0]*1.5
	plt.plot(t,x,'gray',label= 'canddate solutions')	

x_exact = - 5*t**2 + 50*t


plt.plot(t,x_exact,'r',label= 'exact solution')
plt.xlabel('Time(sec)')
plt.ylabel('Distance(meter)')
plt.legend()
plt.grid()
plt.show()
