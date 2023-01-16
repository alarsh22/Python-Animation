import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Creating time array:

t_0 = 0
t_end = 10
dt = 0.02

t = np.arange(t_0,t_end+dt,dt)


r = 3
f = 0.5
x = 0.1*t**2
y = 0*t
z = t
alpha = 2*np.pi*f*t
phi = np.pi/6
############################## ANIMATION ##################
frame_amount = len(t)

def update_plot(num):
    trajectory.set_data(x[0:num],y[0:num])
    trajectory.set_3d_properties(z[0:num])
    X_motion.set_data(t[0:num], x[0:num])
    Y_motion.set_data(t[0:num], y[0:num])
    Z_motion.set_data(t[0:num], z[0:num])

    drone_body_x.set_xdata([x[num]-0.5*np.cos(alpha[num]),x[num]+0.5*np.cos(alpha[num])])
    drone_body_x.set_ydata([y[num]-0.5*np.sin(alpha[num]),y[num]+0.5*np.sin(alpha[num])])
    drone_body_x.set_3d_properties([z[num]+0.5*np.sin(phi),z[num]-0.5*np.sin(phi)])

    drone_body_y.set_xdata([x[num]-0.5*np.cos(alpha[num]+np.pi/2),x[num]+0.5*np.cos(alpha[num]+np.pi/2)])
    drone_body_y.set_ydata([y[num]-0.5*np.sin(alpha[num]+np.pi/2),y[num]+0.5*np.sin(alpha[num]+np.pi/2)])
    drone_body_y.set_3d_properties([z[num],z[num]])



    return trajectory, X_motion, Y_motion, Z_motion, drone_body_x, drone_body_y

fig = plt.figure(figsize=(16,9),dpi=120,facecolor=(0.9,0.9,0.9))
gs = gridspec.GridSpec(3,3)

#Plot-1

Ob1 = fig.add_subplot(gs[:,0:2],projection = '3d',facecolor=(0.9,0.9,0.9))
trajectory, = Ob1.plot([],[],[],'--r',linewidth = 2, label = 'Drone Trajectory')
drone_body_x, = Ob1.plot([],[],[],'b',linewidth=5,label='body-x')
drone_body_y, = Ob1.plot([],[],[],'g',linewidth = 5,label='body-y')
Ob1.set_xlim(-3,3)
Ob1.set_ylim(-3,3)
Ob1.set_zlim(0,7)

Ob1.set_xlabel('X-direction')
Ob1.set_ylabel('Y-direction')
Ob1.set_zlabel('Z-direction')
plt.grid(True)
plt.legend(loc = 'upper right')

# Plot -2
Ob2 = fig.add_subplot(gs[0,2],facecolor = (0.9,0.9,0.9))
X_motion, = Ob2.plot([],[],'aqua',linewidth = 3, label = 'Motion in X')
plt.ylim(min(x)-1,max(x)+1)
plt.xlim(t_0,t_end+1)
plt.ylabel('X_motion [m]')
plt.grid(True)

# Plot -3
Ob3 = fig.add_subplot(gs[1,2],facecolor = (0.9,0.9,0.9))
Y_motion, = Ob3.plot([],[],'b',linewidth = 3, label = 'Motion in Y')
plt.ylim(min(y)-1,max(y)+1)
plt.xlim(t_0,t_end+1)
plt.ylabel('Y_motion [m]')
plt.grid(True)

# Plot -4
Ob4 = fig.add_subplot(gs[2,2],facecolor = (0.9,0.9,0.9))
Z_motion, = Ob4.plot([],[],'g',linewidth = 3, label = 'Motion in Z')
plt.ylim(min(z),max(z)+1)
plt.xlim(t_0,t_end+1)
plt.xlabel('Time [sec]')
plt.ylabel('Z_motion [m]')
plt.grid(True)

ANIMATION = animation.FuncAnimation(fig,update_plot, frames=frame_amount, interval=20,repeat=True,blit=True)
plt.show()