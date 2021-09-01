#These are the python libraries that are going to help us to create a plot
import matplotlib.pyplot as plt
import numpy as np

#This is the function that will be intergrated
def f(x):
    #x**4-2*x+1
    return x**4-2*x+1 

#This 'Trapizoid_Rule' function will require a function,
#'b' value so the lower limit of a integral
#'a' value so the upper limit of a integral
# The amount of NUMERICAL PLOTS.
     
def Trapizoid_Rule(f, xmin, xmax, N):
    #the area has been initially set to 0
    area = 0
    #h is the step size
    h = (xmax-xmin)/N
    
    #the 'arange' function return evenly spaced numbers over a specified interval
    #It takes in the a & b limit parameters and Amount of NUMERICAL PLOTS
    npoints = np.arange(xmin, xmax, h)
    del_dis = np.delete(npoints, 0)
    area = h*((f(xmin)/2)+(f(xmax)/2)+sum(f(xmin+del_dis)))
   
    return area
   
#-----ENTER THE FOLLOWING----
#Function f
#upper limit (a)
#lower limit (b)
#Amount of NUMERICAL PLOTS
    
def integrate(f,a,b,N):
    
    integral = Trapizoid_Rule(f,a,b,N)
    integral2 = Trapizoid_Rule(f,a,b,N/2)
    
    x = np.linspace(a, b, int(N))
    #size of graph
    plt.figure(figsize=(14,7))
    #graph plotting function
    plt.plot(x,f(x),'--o',label=r'$f(x)$') 
    
    #this function fills in the area between the a and b limits 
    plt.fill_between(x,f(x), where =[(x>=a)and(x<=b) for x in x],color= 'gray', alpha = '0.7')
    
    #this function produces lines from the NUMERICAL PLOTS to the x-axis     
    plt.vlines(x, 0, f(x), color='purple', linestyle=':')
    
    ###aixs lines##############
    plt.axhline(color='black')
    plt.axvline(color = 'black')
    ############################
     
    
    ###These are the axis labels######
    plt.ylabel("f(x)",fontsize=16)
    plt.xlabel("x",fontsize = 16)
    
    #this is the little box that displayed the colour of the function
    plt.legend(loc='upper right')
    
    plt.grid(color = 'gray', linewidth=1)
    plt.show()

    error = abs(integral-integral2)/3
    return integral,error

#This is the integrate function, the following parameters can be changed
#first--function--
#second--start time
#third--end time
#fourth--Numerical Plots    
ans,err_est = integrate(f,0,2,1000)
#N=10, Error=0.10613333333333348
#N=100, Error=0.001066613333333244
#N=1000, Error=1.0666661333758043e-05

print('EXACT INTERGRAL=',ans,'||','ESTIMATED ERROR =',err_est)








               
                   
                   
                 
    

