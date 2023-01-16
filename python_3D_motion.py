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

a = 0
b = 0
r = 3
f = 1
x = a + r*np.cos(2*np.pi*f*t)
y = b + r*np.sin(2*np.pi*f*t)
z = t

########################################### ANIMATION ##################
frame_amount = len(t)

def update_plot(num):
    trajectory.set_data(x[0:num],y[0:num])
    trajectory.set_3d_properties(z[0:num])
    X_motion.set_data(t[0:num], x[0:num])
    Y_motion.set_data(t[0:num], y[0:num])
    Z_motion.set_data(t[0:num], z[0:num])

    return trajectory, X_motion, Y_motion, Z_motion

fig = plt.figure(figsize=(16,9),dpi=120,facecolor=(0.9,0.9,0.9))
gs = gridspec.GridSpec(3,3)

#Plot-1

Ob1 = fig.add_subplot(gs[:,0:2],projection = '3d',facecolor=(0.9,0.9,0.9))
trajectory, = Ob1.plot([],[],[],'r',linewidth = 4, label = 'Drone Trajectory')
Ob1.set_xlim(min(x)-1,max(x)+1)
Ob1.set_ylim(min(y)-1,max(y)+1)
Ob1.set_zlim(min(z)-1,max(z)+1)

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
plt.legend(loc = 'upper right')
plt.grid(True)

# Plot -3
Ob3 = fig.add_subplot(gs[1,2],facecolor = (0.9,0.9,0.9))
Y_motion, = Ob3.plot([],[],'b',linewidth = 3, label = 'Motion in Y')
plt.ylim(min(y)-1,max(y)+1)
plt.xlim(t_0,t_end+1)
plt.ylabel('Y_motion [m]')
plt.legend(loc = 'upper right')
plt.grid(True)

# Plot -4
Ob4 = fig.add_subplot(gs[2,2],facecolor = (0.9,0.9,0.9))
Z_motion, = Ob4.plot([],[],'g',linewidth = 3, label = 'Motion in Z')
plt.ylim(min(z),max(z)+1)
plt.xlim(t_0,t_end+1)
plt.xlabel('Time [sec]')
plt.ylabel('Z_motion [m]')
plt.legend(loc = 'upper right')
plt.grid(True)

ANIMATION = animation.FuncAnimation(fig,update_plot, frames=frame_amount, interval=20,repeat=True,blit=True)
plt.show()