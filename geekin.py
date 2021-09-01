def plot_results(time, func):
    plt.plot(time,func,'r--')
    plt.title('Oribital Plot ')
    plt.xlabel('x-displacement')
    plt.ylabel('y-displacement')
    plt.grid(True)
    plt.show()
   

def rk4(f,a,b,N):
    h= b-a/N
    x= a + np.arange(N+1)*h
    y= np.zeros(x.size)
    y0=1
    y[0] = y0
    
    for k in range(1,N):
        k1= f(x[k],y[k])
        k2=f(x[k]+h/2,y[k] +h *k1/2)
        k3=f(x[k]+h/2,y[k] +h *k2/2)
        k4=f(x[k] + h,y[k] + h *k3)
        y[k+1] = y[k] + h *(k1 +2 * (k2+k3)+k4)/6
    return x,y

steps =50
time,func=rk4(f,0,10,steps)

plot_results(time,func)