# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def orbit(u):
    x,y,v_x,v_y = u
    r=np.hypot(x,y)
    #r= 1.521e+06
    #M,G=1.989e+30,6.7e-11
    M,G=20,110
    f=G*M/r**3
    return np.array([v_x,v_y,-f*x,-f*y])


def RK4(f,u,dt):
    k1=f(u)*dt
    k2=f(u+0.5*k1)*dt
    k3=f(u+0.5*k2)*dt
    k4=f(u+k3)*dt
    return u+(k1+2*k2+2*k3+k4)/6

    
def RK4_int(f,y0,tspan):
    y=np.zeros([len(tspan),len(y0)])
    y[0,:] =y0
    for k in range (1,len(tspan)):
        y[k,:] = RK4(f,y[k-1],tspan[k]-tspan[k-1])
    return y

dt=0.1
t = np.arange(0,10,dt)
y0=np.array([10, 0.0, 10, 10])

sol_rk4=RK4_int(orbit,y0,t)
x,y,v_x,v_y = sol_rk4.T
plt.grid()
plt.plot(x,y)
plt.show()
