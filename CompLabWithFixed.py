import numpy as np
import matplotlib.pyplot as plt
from time import time

#########Constants############
sun_mass = 1.989e+30  
G = 66374.2  
x_0 = 4e+12
y_0 = 0
v_x = 0
v_y = 15768000000 
t_0 = 0
t_f = 165 #year
t0=time()
###############################
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

#----This is the fixed step size method---
tpoints = np.arange(t_0, t_f, h)
xpoints = []
ypoints = []
r = np.array([x_0, v_x, y_0, v_y], float)
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[2])
    k1 = h * f(r, t)
    k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
    k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
    k4 = h * f(r + k3, t + h)
    r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    #calculate time to compute
    dt=time()-t0
    
plt.plot(np.array(xpoints, float) / 1e3, np.array(ypoints, float) / 1e3)
plt.title("Comet Orbiting Sun")
plt.xlabel('X Displacement (km)')
plt.ylabel('Y Displacement (km)')
print("it took",round(dt,3),"seconds to compute")
plt.grid()
plt.show()

    
    
    
    
    
