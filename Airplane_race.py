import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

t0=0
t_end=2 #hrs
dt=0.005 #hrs

#Array for time
t=np.arange(t0,t_end+dt,dt)

# Airplane - 1

    # Array for x-distance
a1 = 800
b1 = 1
x1=a1*t**b1


altitude1 = 2.5 # km
# Creating y array
y1 = np.ones(len(t))*altitude1

speed_x1 = b1*a1*t**(b1-1)

#Airplane - 2

# Array for x-distance
a2 = 1600/2**0.5
b2 = 0.5
x2=a2*t**b2


altitude2 = 1.5 # km

# Creating y array
y2 = np.ones(len(t))*altitude2
if b2<1:
    t[0]=t[1]
speed_x2 = b2*a2*t**(b2-1)

#Airplane - 3

 # Array for x-distance
a3 = 200
b3 = 3
x3=a3*t**b3

altitude3 = 0.5 # km

# Creating y array
y3 = np.ones(len(t))*altitude3

speed_x3 = b3*a3*t**(b3-1)

######################### Animation ###########################

frame_amount = int(len(t))

# Loop for Airplane -1
dot1 = np.zeros(frame_amount)
n=20
# loop for creating the trailing dots behind the airplane
for i in range(0,frame_amount):
    if i == n:
        dot1[i] = x1[i]
        n=n+20

    else:
        dot1[i] = x1[n-20]

# Loop for Airplane - 2
dot2 = np.zeros(frame_amount)
n=20
for i in range(0,frame_amount):
    if i == n:
        dot2[i] = x2[i]
        n=n+20

    else:
        dot2[i] = x2[n-20]

# Loop for Airplane - 3
dot3 = np.zeros(frame_amount)
n=20
for i in range(0,frame_amount):
    if i == n:
        dot3[i] = x3[i]
        n=n+20

    else:
        dot3[i] = x3[n-20]


def update_plot(num):

    # 1st Subplot
    # Airplane -1
    plane1_trajectory.set_data(dot1[0:num],y1[0:num])
    plane1_fuselage.set_data([x1[num]-50,x1[num]+50],[y1[num],y1[num]])
    plane1_up_wing.set_data([x1[num]+25,x1[num]], [y1[num], y1[num] + 0.4])
    plane1_low_wing.set_data([x1[num]+25, x1[num]], [y1[num], y1[num] - 0.4])
    plane1_up_stablizer.set_data([x1[num] - 35, x1[num]-50], [y1[num], y1[num] + 0.2])
    plane1_low_stablizer.set_data([x1[num] - 35, x1[num]-50], [y1[num], y1[num] - 0.2])

    # Airplane - 2
    plane2_trajectory.set_data(dot2[0:num], y2[0:num])
    plane2_fuselage.set_data([x2[num] - 50, x2[num] + 50], [y2[num], y2[num]])
    plane2_up_wing.set_data([x2[num] + 25, x2[num]], [y2[num], y2[num] + 0.4])
    plane2_low_wing.set_data([x2[num] + 25, x2[num]], [y2[num], y2[num] - 0.4])
    plane2_up_stablizer.set_data([x2[num] - 35, x2[num] - 50], [y2[num], y2[num] + 0.2])
    plane2_low_stablizer.set_data([x2[num] - 35, x2[num] - 50], [y2[num], y2[num] - 0.2])

    # Airplane - 3
    plane3_trajectory.set_data(dot3[0:num], y3[0:num])
    plane3_fuselage.set_data([x3[num] - 50, x3[num] + 50], [y3[num], y3[num]])
    plane3_up_wing.set_data([x3[num] + 25, x3[num]], [y3[num], y3[num] + 0.4])
    plane3_low_wing.set_data([x3[num] + 25, x3[num]], [y3[num], y3[num] - 0.4])
    plane3_up_stablizer.set_data([x3[num] - 35, x3[num] - 50], [y3[num], y3[num] + 0.2])
    plane3_low_stablizer.set_data([x3[num] - 35, x3[num] - 50], [y3[num], y3[num] - 0.2])


    # 2nd subplot
    x1_dist.set_data(t[0:num],x1[0:num])
    x2_dist.set_data(t[0:num],x2[0:num])
    x3_dist.set_data(t[0:num],x3[0:num])

    # 3rd Subplot

    speed1.set_data(t[0:num],speed_x1[0:num])
    speed2.set_data(t[0:num],speed_x2[0:num])
    speed3.set_data(t[0:num],speed_x3[0:num])


    return plane1_trajectory,plane1_fuselage,plane1_up_wing,plane1_low_wing,plane1_up_stablizer,plane1_low_stablizer,\
           plane2_trajectory,plane2_fuselage,plane2_up_wing,plane2_low_wing,plane2_up_stablizer,plane2_low_stablizer,\
           plane3_trajectory,plane3_fuselage,plane3_up_wing,plane3_low_wing,plane3_up_stablizer,plane3_low_stablizer,\
           x1_dist,x2_dist,x3_dist,speed1,speed2,speed3

fig = plt.figure(figsize = (16,9),dpi = 120,facecolor = (0.9,0.9,0.9))
gs = gridspec.GridSpec(2,2)

# Creating Subplot - 1:
ax0 = fig.add_subplot(gs[0,:],facecolor=(0.4,0.9,0.9))
# Airplane - 1
plane1_trajectory, = ax0.plot([],[],'r:*',linewidth = 2)
# Creating Airplane Body
plane1_fuselage, = ax0.plot([],[],'k',linewidth = 7)
plane1_up_wing, = ax0.plot([],[],'k',linewidth = 5)
plane1_low_wing, = ax0.plot([],[],'k',linewidth = 5)
plane1_up_stablizer, = ax0.plot([],[],'k',linewidth = 5)
plane1_low_stablizer, = ax0.plot([],[],'k',linewidth = 5)

# Airplane - 2
plane2_trajectory, = ax0.plot([],[],'b:*',linewidth = 2)
# Creating Airplane Body
plane2_fuselage, = ax0.plot([],[],'k',linewidth = 7)
plane2_up_wing, = ax0.plot([],[],'k',linewidth = 5)
plane2_low_wing, = ax0.plot([],[],'k',linewidth = 5)
plane2_up_stablizer, = ax0.plot([],[],'k',linewidth = 5)
plane2_low_stablizer, = ax0.plot([],[],'k',linewidth = 5)

# Airplane - 3
plane3_trajectory, = ax0.plot([], [], 'g:*', linewidth=2)
# Creating Airplane Body
plane3_fuselage, = ax0.plot([], [], 'k', linewidth=7)
plane3_up_wing, = ax0.plot([], [], 'k', linewidth=5)
plane3_low_wing, = ax0.plot([], [], 'k', linewidth=5)
plane3_up_stablizer, = ax0.plot([], [], 'k', linewidth=5)
plane3_low_stablizer, = ax0.plot([], [], 'k', linewidth=5)

copyright=ax0.text(0,(altitude1+0.7),'© AL ARSH BASHEER',size=15)

# Subplot Properties
plt.xlim(x1[0],x1[-1])
plt.ylim(0,y1[0]+0.5)
plt.xticks(np.arange(x1[0],x1[-1]+1,x1[-1]/4),size=15)
plt.yticks(np.arange(0,y1[-1]+1,y1[-1]/y1[-1]),size=15)
plt.xlabel('x distance [km]',fontsize = 10)
plt.ylabel('y distance [km]',fontsize = 10)
plt.title('Airplane animation',fontsize = 20)
plt.grid(True)

# Creating Subplot 2
ax1 = fig.add_subplot(gs[1,0],facecolor=(0.9,0.9,0.9))
x1_dist, = ax1.plot([],[],'-r',linewidth = 2, label = 'X ='+str(a1)+str('*t^')+str(b1))
x2_dist, = ax1.plot([],[],'-b',linewidth = 2, label = 'X ='+str(round(a2))+str('*t^')+str(b2))
x3_dist, = ax1.plot([],[],'-g',linewidth = 2, label = 'X ='+str(round(a3))+str('*t^')+str(b3))

# Subplot 2 properties
plt.xlim(0,t[-1])
plt.ylim(x1[0],x1[-1])
plt.xticks(np.arange(0,t[-1]+0.00001,t[-1]/4),size=10)
plt.yticks(np.arange(x1[0],x1[-1]+1,x1[-1]/4),size=10)
plt.xlabel('Time',fontsize = 15)
plt.ylabel('Distance [km]',fontsize = 15)
plt.grid(True)
plt.legend(loc='upper left',fontsize='x-large')

# Creating Subplot 3
ax2 = fig.add_subplot(gs[1,1],facecolor=(0.9,0.9,0.9))
speed1, = ax2.plot([],'-r', linewidth = 2)
speed2, = ax2.plot([],'-b', linewidth = 2)
speed3, = ax2.plot([],'-g', linewidth = 2)


# Subplot 3 Properties
plt.xlim(0,t[-1])
plt.ylim(0,speed_x1[-1]*2)
plt.grid(True)
plt.xticks(np.arange(0,t[-1]+0.00001,t[-1]/4),size = 10)
plt.yticks(np.arange(0,speed_x1[-1]*2+1,speed_x1[-1]*2/4),size=10)
plt.xlabel('Time [hr]')
plt.ylabel('Speed [km/hr]')

plane_ani=animation.FuncAnimation(fig,update_plot,frames=frame_amount,interval=20,repeat=False,blit=True)
plt.show()
