import numpy as np
import matplotlib.pyplot as plt

###########THE FUNCTIONS###########################################

####Task1 Equation (dy/dt=-2x)####################################
def f(x,T):   
    return -2*x

#####Task 1 analytical soltution##################################
def f1():
    x0 = 1
    #change the second parameter of the x_a function to change the endtime of the analytical solution
    x_a = np.arange(0,5,0.01)
    y_a =x0*np.exp(-2*(x_a))
    
    return x_a, y_a

######Task2 Equation (dy/dt=2-2X-e^-4t)############################
def f2(x,T):
    e=np.exp(-4*T)
    #2-2*x-e**-4*T
    return 2-(2*x)-e

######Task 2 analytical soltution################################
def f3():
    #change the second parameter of the t function to change the endtime of the analytical solution
    t= np.arange(0,5,0.01)
    y2_a = 1 +((1/2)*(np.exp(-4*t)))-((1/2)*(np.exp(-2*t)))  
    return t,y2_a
####################################################################

#This 'euler' function will require a function which are displayed above,
#A initial condition (in this case x(0)= 1)
#A start point, which is currently 0
# The amount of NUMERICAL PLOTS. (in this case it ranges from 50-5000 points)
                   
def euler(f,x0,S,T,npoints):  
      
    #time step
    h=(T-S)/npoints
          
    #the 'linspace' function return evenly spaced numbers over a specified interval
    #It takes in the Start parameter,End parameter and Amount of NUMERICAL PLOTS
    t=np.linspace(S,T,npoints)
    # the 'x' varible will contain 't' amount of values. These values will be 0.
    x = np.zeros(len(t))
    
    #This sets the 1st item  of the 'x' list to the initial condition 
    x[0]=x0
    #This is the for loop which will produce the the points required for the graph 
    for i in range(1, len(t)):  
        x[i]=x[i-1] + f(x[i-1],t[i])*h
 
    #size of graph
    plt.figure(figsize=(12,7))
    
    return x,t,

#Here you have 2 functions that are being passes through the euler function
#The parameters of the euler function can be changed 
#the first parameter:---function---
#second parameter:---Intial condition---
#Third parameter:---Start time---
#Fourth parameter: ---End time---
#Fifth parameter: ---Amount of numerical plots---
#(If you want to change the time of the analytical soltution,
#scroll to the analytical soltution function 1 or 2  and change the SECOND PARAMETER OF THE
#np.arange(...) function)
    
f1plot,t1, = euler(f,1,0,5,50)

f2plot,t2 = euler(f2,1,0,5,50)

#this part plots the function that is shown on the 2 previous lines
plt.plot(t1,f1plot,'o--',t2,f2plot,'o--',label=r'$f(x)$')

#the analytical solutions are passed through this function
t_t1, an_plot = f1()
t_t2, an2_plot = f3()

#these are where the analytical solutions are plotted
plt.plot(t_t1,an_plot,'r--',t_t2,an2_plot,'g--')
plt.legend(('f(x)|1','f(x)|2','An_sol|1','An_sol|2'),loc='upper right')

###These are the axis labels######
plt.ylabel('X AS A FUNCTION OF T')
plt.xlabel('time')
##################################

######These Are the x & y axises thart are displayed on the graph###
plt.axhline(color='black')
plt.axvline(color ='black')
####################################################################
#grid function that places a grid on the graph 
plt.grid(linewidth=2)
