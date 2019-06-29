import numpy as np
import matplotlib.pyplot as plt
from numpy import ma

def f(x,y):
    global a, b
    ans = b*x*(1-x) - (a*x*y)/(0.5+x)
    return ans

def g(x,y):
    global d
    ans = (x*y)/(0.5+x) - d*y
    return ans

def eular(x0, y0, h, T):
    global a,b,d
    n = int(T/h)
    x = np.zeros(int(n))
    y = np.zeros(int(n))
    x[0] = x0; y[0]=y0
    # x
    for i in range(1,n):
        x[i] = x[i-1] + h*f(x[i-1],y[i-1])
        y[i] = y[i-1] + h*g(x[i-1],y[i-1])
    return x, y

# Assumptions: 
a = 3.0
b = 1.0
d = 0.35
T = 200     # time
h = 0.05    # time step

# Initial Conditions:
x0 = 0.5
y0 = 0.6


X, Y = np.meshgrid(np.arange(0, 1, .05), np.arange(0, 1, .05))
U = f(X,Y)
V = g(X,Y)

plt.figure(1)
Q = plt.quiver(X, Y, U, V, units='width')


x0 = 0.5; y0 = 0.6
T = 200
h = 0.05


xp , yp = eular(x0, y0, h, T)
plt.plot(xp,yp,label = "Particular Solution")
plt.figure(1)
plt.title("System field  (a="+str(a)+", b="+str(b)+", d="+str(d)+", x0="+str(x0)+", y0="+str(y0)+")")
plt.figure(2)
plt.plot(xp,'r:',label="Prey Density")
plt.plot(yp,'k-',label="Predator Density")
plt.xlabel("Time")
plt.ylabel("Density")
plt.legend(loc="best")
x3 = 0.5*d/(1-d)
y3 = b*(1-x3)*(.5+x3)

xnull_x = np.arange(0, 1,.05)
ynull_x = (b/a)*(0.5+xnull_x)*(1-xnull_x)
ynull_y =  np.arange(0, 1,.05)
xnull_y = np.zeros(len(ynull_y)) + (0.5*d)/(1-d)

plt.title("Predator-Prey density (a="+str(a)+", b="+str(b)+", d="+str(d)+", x0="+str(x0)+", y0="+str(y0)+")")
plt.figure(1)
plt.plot(xnull_x, ynull_x,label = "Prey Null-cline")
plt.plot(xnull_y,ynull_y,label="Predator null-cline")
plt.xlabel("Prey Population density")
plt.ylabel("Predator Population Density")
plt.xlim(0,1)
plt.ylim(0,1)
plt.legend(loc="upper right")
plt.show()