# -*- coding: utf-8 -*-
import numpy as np
from numpy import sin,cos
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#define equations
def eqns(y0, t):
    theta,x=y0
    f = [x,-(g/l)*sin(theta)]
    return f

def plot_results(time, theta_1,theta_2):
    plt.plot(time, theta_1[:,0])
    plt.plot(time, theta_2)
    s= ('Inital angle= ' + str(angle) + ' degrees')
    plt.title('Pendulum motion: ' + s)
    plt.xlabel('time(s)')
    plt.ylabel('angle (radians)')
    plt.grid(True)
    plt.legend(['non linear','linear'], loc='lower right')
    plt.show()

#parameters
g = 9.81
l = 10

time = np.arange(0,10,0.02)

#inital conditions
angle = 130
theta_0=np.radians(angle)
x0 = np.radians(0)

#non anylitcal solution
theta_1= odeint(eqns,[theta_0,x0], time)

#analytical
w=np.sqrt(g/l)
theta_2= [theta_0*cos(w*t)for t in time ] 

#plot results
plot_results(time, theta_1,theta_2)