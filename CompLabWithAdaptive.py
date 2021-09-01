#Constants
sun_mass = 1.989 * 10 ** 30  
import numpy as np
import matplotlib.pyplot as plt
from time import time

G = 66374.2 
x_0 = 4 * 10 ** 12  # m
y_0 = 0
v_x = 0
v_y = 15768000000 
t_0 = 0
t_f = 165  # years
t0=time()

N = 200000
h = (t_f - t_0) / N

def f(r, t):
    x = r[0]
    y = r[2]
    v_x = r[1]
    v_y = r[3]
    #distance
    dist = np.sqrt(x**2 + y**2)
    #return the first order equations
    return np.array([v_x, - G * sun_mass * x / dist ** 3, v_y, - G * sun_mass * y / dist ** 3], float)

#Runge Kutta 
def RK4(r, t, h):
        k1 = h * f(r, t)
        k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
        k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
        k4 = h * f(r + k3, t + h)
        return (k1 + 2 * k2 + 2 * k3 + k4) / 6

#----------adaptive stepsize--------
def t_step(r, t, h):
    # perform 2 Runge Kutta steps of step size h
    d_step_1 = RK4(r, t, h)
    d_step_2 = RK4(r + d_step_1, t + h, h)
    d_r1 = d_step_1 + d_step_2

    # perform 1 Runge kutta steps with step size 2h
    d_r2 = RK4(r, t, 2 * h)

    # Ccalculate the error estimate
    d_x1 = d_r1[0]
    d_x2 = d_r2[0]
    d_y1 = d_r1[2]
    d_y2 = d_r2[2]
    error = np.sqrt((d_x1 - d_x2) ** 2 + (d_y1 - d_y2) ** 2) / 30

    # Calculate rho value
    
    with np.errstate(divide='ignore'):
        rho = h * delta / error
        
    # Calculate factor 
    factor = np.power(rho, 1 / 4)
    
    # Ithe f target accuracy is met,go to next step
    if  rho >= 1:
        # update value of t
        t += 2*h

        if factor > 2:
            h *= 2
        else:
            h *= factor
            
        d_r1[0] += (d_x1 - d_x2) / 15
        d_r1[2] += (d_y1 - d_y2) / 15
        return d_r1, h, t
    # If target accuracy isnt met then redo calcuation with smaller h
    else:
        return t_step(r, t, factor * h)

delta = 1000   
h = (t_f - t_0) / 150000  # initial step size
tpoints = []
xpoints2 = []
ypoints2 = []

# These are the initial conditions
r = np.array([x_0, v_x, y_0, v_y], float)  
t = t_0
while(t < t_f):
    tpoints.append(t)
    xpoints2.append(r[0])
    ypoints2.append(r[2])
    d_r, h, t = t_step(r, t, h)
    r += d_r
    #calculate time to compute
    dt=time()-t0
    
#-----------plotting fucntions------------------
    
plt.plot(np.array(xpoints2, float) / 1e3, np.array(ypoints2, float) / 1e3, 'b')
plt.plot(np.array(xpoints2, float)[::20] / 1e3, np.array(ypoints2[::20], float) / 1e3, 'ro')
plt.title("Comet Orbiting Sun")
print("it took",round(dt,3),"seconds to compute")
plt.xlabel('X Displacement (km)')
plt.ylabel('Y Displacement (km)')
plt.grid()
plt.show()
    
