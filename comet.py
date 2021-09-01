import numpy as np
import matplotlib.pyplot as plt







def rk4(f,r,t,h):
    k1=h*f(r,t)
    k2=h*f(r+0.5*k1,t+0.5*h)
    k3=h*f(r+0.5*k2,t+0.5*h)
    k4=h*f(r+k3,t+h)
    return r + (k1+2*k2+2*k3+k4)/6

h=0.0068
a = 0
b=6.8

