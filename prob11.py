'''
coded by: rakeeb 
coded for: solving simultaneous differential equation
** We can do the problem vectorically which I will try to do later.
'''
import numpy as np 
import matplotlib.pyplot as plt 

t= np.arange(0,1.01,0.01)
u1= np.zeros(101)
u2= np.zeros(101)
u3= np.zeros(101)
h= 0.01

u1[0]= 3
u2[0]= -1
u3[0]= 1

def f1(a,b,c,d):   # a=t, b=u1, c=u2, d=u3
	return(b + 2*c - 2*d + np.exp(-a))

def f2(a,b,c,d):   # a=t, b=u1, c=u2, d=u3
	return(c + d - 2*np.exp(-a))   

def f3(a,b,c,d):   # a=t, b=u1, c=u2, d=u3
	return(b + 2*c + np.exp(-a))		


for i in range(100):
	k10= h*f1(t[i], u1[i], u2[i], u3[i])
	k20= h*f2(t[i], u1[i], u2[i], u3[i])
	k30= h*f3(t[i], u1[i], u2[i], u3[i])

	k11= h*f1(t[i]+h/2, u1[i]+k10/2, u2[i]+k20/2, u3[i]+k30/2)
	k21= h*f2(t[i]+h/2, u1[i]+k10/2, u2[i]+k20/2, u3[i]+k30/2)
	k31= h*f3(t[i]+h/2, u1[i]+k10/2, u2[i]+k20/2, u3[i]+k30/2)

	k12= h*f1(t[i]+h/2, u1[i]+k11/2, u2[i]+k21/2, u3[i]+k31/2)
	k22= h*f2(t[i]+h/2, u1[i]+k11/2, u2[i]+k21/2, u3[i]+k31/2)
	k32= h*f3(t[i]+h/2, u1[i]+k11/2, u2[i]+k21/2, u3[i]+k31/2)

	k13= h*f1(t[i]+h, u1[i]+k12, u2[i]+k22, u3[i]+k32)
	k23= h*f2(t[i]+h, u1[i]+k12, u2[i]+k22, u3[i]+k32)
	k33= h*f3(t[i]+h, u1[i]+k12, u2[i]+k22, u3[i]+k32)

	u1[i+1]= u1[i] + (k10 + 2*k11 + 2*k12 + k13)/6
	u2[i+1]= u2[i] + (k20 + 2*k21 + 2*k22 + k23)/6
	u3[i+1]= u3[i] + (k30 + 2*k31 + 2*k32 + k33)/6

	
plt.plot(t,u1,'r',label='u1')
plt.plot(t,u2,'b',label='u2')
plt.plot(t,u3,'g',label='u3')
plt.xlabel('t')
plt.legend()
plt.grid()
plt.show()	


