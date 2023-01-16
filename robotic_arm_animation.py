import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import matplotlib.animation as animation
# from mpl_toolkits.mplot3d import Axes3D

t_0 = 0
t_end = 1
dt = 0.005

t = np.arange(t_0,t_end+dt,dt)

#First arm:
r1 = 2
f1 = 1
theta1 = 2*np.pi*f1*t
x1 = r1*np.cos(np.pi/2+theta1)
y1 = r1*np.sin(np.pi/2+theta1)

#Second Arm:
r2 = 3
f2 = 1
theta2 = 2*np.pi*f2*t
del_x = r2*np.cos(theta1+theta2)
del_y = r2*np.sin(theta1+theta2)

x2 = x1+ del_x
y2 = y1 + del_y

#Third Arm:
r3 = 2
f3 = 3
theta3 = 2*np.pi*f3*t
del_x2 = r3*np.cos(theta1+theta2+theta3)
del_y2 = r3*np.sin(theta1+theta2+theta3)

x3 = x1 + del_x + del_x2
y3 = y1 + del_y +del_y2

################## ANIMATION ############################

frame_amount = len(t)

def update_plot (num):
    lower_arm.set_data([0,x1[num]],[0,y1[num]])
    upper_arm.set_data([x1[num],x2[num]],[y1[num],y2[num]])
    third_arm.set_data([x2[num],x3[num]],[y2[num],y3[num]])
    trajectory.set_data(x3[0:num],y3[0:num])
    lower_limb_motion.set_data(t[0:num],x1[0:num])
    theta1_func.set_data(t[0:num],theta1[0:num])
    theta2_func.set_data(t[0:num],theta2[0:num])

    return lower_arm, upper_arm, trajectory, lower_limb_motion, theta1_func, theta2_func, third_arm

Fig = plt.figure(figsize= (16,9),dpi=120,facecolor=(0.9,0.9,0.9))
plt.subplots_adjust(left=0.05,right=0.95,bottom=0.07,top=0.95)
GS = gridspec.GridSpec(3,3)

Ob1 = Fig.add_subplot(GS[:,0:2],facecolor = (0.9,0.9,0.9))

#Creating lower arm:
lower_arm, = Ob1.plot([],[],'k',linewidth = 4,label = 'Lower limb')
upper_arm, = Ob1.plot([],[],'b',linewidth = 2,label = 'Upper Limb')
third_arm, = Ob1.plot([],[],'g',linewidth = 1, label = 'Smallest Arm')

# Creating the base of the robot:
base = Ob1.plot([0,0],[0,0.3],'k',linewidth = 15)

# Creating tip of the robot trajectory:
trajectory, = Ob1.plot([],[],'r',linewidth =1)

Ob1.spines['left'].set_position('center')
Ob1.spines['bottom'].set_position('center')
plt.xlabel('X-motion')
Ob1.xaxis.set_label_coords(0.5,-0.01)
plt.ylabel('Y-motion')
Ob1.yaxis.set_label_coords(-0.02,0.5)

plt.xlim(-10,10)
plt.ylim(-10,10)
plt.xticks(np.arange(-10,10+1,1))
plt.yticks(np.arange(-10,10+1,1))

plt.grid(True)
plt.legend(loc='upper right')

# Creating Sub Plot-2:
Ob2 = Fig.add_subplot(GS[0,2], facecolor = (0.9,0.9,0.9))
lower_limb_motion, = Ob2.plot([],[],'b',linewidth = 2)
plt.ylabel('Lower Limb motion [m]')
plt.xlim(t_0,t_end+1)
plt.ylim(min(x1)-1,max(x1)+1)
Ob2.yaxis.set_label_coords(1.1,0.5)
plt.grid(True)

# Creating Sub Plot-3 (for theta-1):
Ob3 = Fig.add_subplot(GS[1,2], facecolor = (0.9,0.9,0.9))
theta1_func, = Ob3.plot([],[],'b',linewidth = 2)
plt.ylabel('theta-1 [rad]')
plt.xlim(t_0,t_end+1)
plt.ylim(0,6*np.pi)
plt.yticks(np.arange(0,6*np.pi+1,np.pi),['0','π','2π','3π','4π','5π','6π'])
Ob3.yaxis.set_label_coords(1.1,0.5)
plt.grid(True)

# Creating Sub Plot-4 (for theta-2):
Ob4 = Fig.add_subplot(GS[2,2], facecolor = (0.9,0.9,0.9))
theta2_func, = Ob4.plot([],[],'b',linewidth = 2)
plt.ylabel('theta-2 [rad]')
plt.xlim(t_0,t_end+1)
plt.ylim(0,6*np.pi)
plt.yticks(np.arange(0,6*np.pi+1,np.pi),['0','π','2π','3π','4π','5π','6π'])
Ob4.yaxis.set_label_coords(1.1,0.5)
plt.xlabel('Time [sec]')
plt.grid(True)

ANIMATION = animation.FuncAnimation(Fig,update_plot,frames=120,interval=20,repeat=True,blit=True)
plt.show()