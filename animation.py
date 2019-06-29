import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

def f(x,y):
    global a, b
    ans = b*x*(1-x) - (a*x*y)/(0.5+x)
    return ans

def null(x,y):
    return 0

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
d = 0.7
T = 200     # time
h = 0.05    # step_size

# Initial Conditions:
x0 = 0.4
y0 = 0.3

# Initializing/Defining figure for animation
fig = plt.figure()
ax = plt.axes(xlim=(0, 1), ylim=(0, 1))
line_y, = ax.plot([], [], lw=2,label="Predator null cline")
line_x, = ax.plot([], [], lw=2,label="Prey null cline")
line_p, = ax.plot([], [], lw=2,label="Particular Solution")
plt.title("System field  (a="+str(a)+", b="+str(b)+", d="+str(d)+", x0="+str(x0)+", y0="+str(y0)+")")
plt.xlabel("Prey Population density")
plt.ylabel("Predator Population Density")

# Calculation of System field
X, Y = np.meshgrid(np.arange(0, 1, .05), np.arange(0, 1, .05))
U = f(X,Y)
V = g(X,Y)
Q = ax.quiver(X, Y, U, V, units='width')
ax.legend(loc="upper right")


# initialization function:
def init():
    line_y.set_data([], [])
    line_x.set_data([], [])
    line_p.set_data([], [])
    return line_y, line_x, line_p

# animation function.
def animate(i):

    global a,b,d,Q,X,Y,x0,y0,h,T

    d = 0.7 * (200-i)/200       # Animation will animate according to this parameter change

    # Calculation of System field
    U = f(X,Y)
    V = g(X,Y)
    Q.set_UVC(U,V)

    # Calculation for Perticular initial conditions
    xp , yp = eular(x0, y0, h, T)
    line_p.set_data(xp,yp)

    # Calculation of null clines
    xnull_x = np.arange(0, 1,.05)
    ynull_x = (b/a)*(0.5+xnull_x)*(1-xnull_x)
    ynull_y =  np.arange(0, 1,.05)
    xnull_y = np.zeros(len(ynull_y)) + (0.5*d)/(1-d)
    line_y.set_data(xnull_y,ynull_y)
    line_x.set_data(xnull_x,ynull_x)


    return line_y, line_x, Q,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=150, interval=20, blit=False)

anim.save('basic_animation.mp4', fps=10, extra_args=['-vcodec', 'libx264'])

plt.show()