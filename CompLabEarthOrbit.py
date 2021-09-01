import numpy as np
import matplotlib.pyplot as plt

x_0 = 0
y_0 = 0
v_x = 0
v_y = 0
sun_mass=1.989e+30
G=6.7e-11

def f(r,t):
    x = r[0]
    y = r[2]
    v_x = r[1]
    v_y = r[3]
    #distance
    dist = np.sqrt(x**2 + y**2)
    #return the first order equations
    return np.array([v_x, - G * sun_mass * x / dist ** 3, v_y, - G * sun_mass * y / dist ** 3], float)


###########time periods#################
a=0
#Over 1 year
b= 365*24*60*60
#over 10 years
#b= 10*365*24*60*60

#Over a week
#h=7*24*60*60

#One Hour
h=60*60

#Over a month
#h=30*24*60*60
############################
tpoints = np.arange(a, b, h)
r = np.array([x_0, v_x, y_0, v_y], float)

def RK4(f,h,tpoints,r):
    xpoints = []
    ypoints = []
    zpoints = []    
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[2])
        zpoints.append(np.sqrt(r[1]**2+r[3]**2))
        k1 = h * f(r, t)
        k2 = h * f(r + 0.5 * k1, t + 0.5 * h)
        k3 = h * f(r + 0.5 * k2, t + 0.5 * h)
        k4 = h * f(r + k3, t + h)
        r += (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return np.array(xpoints,float), np.array(ypoints,float),np.array(zpoints,float)


xpoints,ypoints,zpoints = RK4(f,h,tpoints,[152.1e+09, 0, 0, 29.3e+03])

plt.plot(xpoints/1e9, ypoints/1e9,'.b')
plt.title("Earth Orbiting Sun")
plt.xlabel('X Displacement (km)')
plt.ylabel('Y Displacement (km)')
plt.grid()
plt.show()

plt.plot(tpoints,zpoints)
plt.title("Orbital Speed Over Time")
plt.xlabel('X Displacement (km)')
plt.ylabel('Y Displacement (km)')
plt.grid()
plt.show()