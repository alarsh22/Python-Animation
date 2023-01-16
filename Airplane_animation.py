import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

t0=0
t_end=2 #hrs
dt=0.005 #hrs

#Array for time
t=np.arange(t0,t_end+dt,dt)

# Array for x-distance
a = 200
b = 3
x=a*t**b


altitude = 2 # km


# Creating y array
y = np.ones(len(t))*altitude

speed_x = b*a*t**(b-1)

######################### Animation ###########################

frame_amount = int(len(t))
dot = np.zeros(frame_amount)
n=20
# loop for creating the trailing dots behind the airplane
for i in range(0,frame_amount):
    if i == n:
        dot[i] = x[i]
        n=n+20

    else:
        dot[i] = x[n-20]


def update_plot(num):

    # 1st Subplot
    plane_trajectory.set_data(dot[0:num],y[0:num])
    plane_fuselage.set_data([x[num]-50,x[num]+50],[y[num],y[num]])
    plane_up_wing.set_data([x[num]+25,x[num]], [y[num], y[num] + 0.4])
    plane_low_wing.set_data([x[num]+25, x[num]], [y[num], y[num] - 0.4])
    plane_up_stablizer.set_data([x[num] - 35, x[num]-50], [y[num], y[num] + 0.2])
    plane_low_stablizer.set_data([x[num] - 35, x[num]-50], [y[num], y[num] - 0.2])
    text_ax0.set_text(str(round(t[num],1))+ ' hr')
    text_x_value.set_text('x Distance ='+ str(round(x[num],1))+ ' km')
    text_y_value.set_text('Altitude ='+ str(round(y[num],1))+ ' km')
    plane_vertical.set_data([x[num],x[num]],[0,y[num]])

    # 2nd subplot
    x_dist.set_data(t[0:num],x[0:num])
    vertical_line.set_data([t[num], t[num]], [x[0], x[num]])
    horizontal_line.set_data([t[0],t[num]],[x[num],x[num]])

    # 3rd Subplot

    speed.set_data(t[0:num],speed_x[0:num])
    vertical_ax2.set_data([t[num],t[num]],[0,speed_x[num]])
    if num!=0:
        #text_numerator.set_text(str(round(x[num])))
        #text_denominator.set_text(str(round(t[num],3)))
        text_ans.set_text('dx/dt = '+str(round(speed_x[num]))+'km/hr')

    return plane_trajectory,plane_fuselage,plane_up_wing,plane_low_wing,\
           plane_up_stablizer,plane_low_stablizer,plane_vertical,text_ax0,text_x_value,x_dist,\
vertical_line,horizontal_line, speed,vertical_ax2,text_numerator,text_denominator,text_ans

fig = plt.figure(figsize = (16,9),dpi = 120,facecolor = (0.9,0.9,0.9))
gs = gridspec.GridSpec(2,2)

# Creating Subplot - 1:
ax0 = fig.add_subplot(gs[0,:],facecolor=(0.4,0.9,0.9))
plane_trajectory, = ax0.plot([],[],'g:*',linewidth = 2, label = 'dist. covered in 0.1 hr')
plane_vertical, = ax0.plot([],[],'k:o', linewidth = 2)
# Creating Airplane Body
plane_fuselage, = ax0.plot([],[],'k',linewidth = 7)
plane_up_wing, = ax0.plot([],[],'k',linewidth = 5)
plane_low_wing, = ax0.plot([],[],'k',linewidth = 5)
plane_up_stablizer, = ax0.plot([],[],'k',linewidth = 5)
plane_low_stablizer, = ax0.plot([],[],'k',linewidth = 5)

# Draw buildings
plane_B1 = ax0.plot([100,100],[0,0.7],'b',linewidth = 10)
plane_B2 = ax0.plot([600,600],[0,1],'b',linewidth = 12)
plane_B3 = ax0.plot([1550,1550],[0,1.2],'b',linewidth = 9)
plane_B4 = ax0.plot([1000,1000],[0,0.9],'b',linewidth = 9)
plane_B5 = ax0.plot([1400,1400],[0,1.4],'b',linewidth = 11)

copyright=ax0.text(0,(altitude+1.07),'© AL ARSH BASHEER',size=15)

# Subplot Properties
plt.xlim(x[0],x[-1])
plt.ylim(0,y[0]+1)
plt.xticks(np.arange(x[0],x[-1]+1,x[-1]/4),size=15)
plt.yticks(np.arange(0,y[-1]+2,y[-1]/y[-1]),size=15)
plt.xlabel('x distance [km]',fontsize = 10)
plt.ylabel('y distance [km]',fontsize = 10)
plt.title('Airplane animation',fontsize = 20)
plt.grid(True)
plt.legend(loc='upper right',fontsize=15)

# Creating Subplot 2
ax1 = fig.add_subplot(gs[1,0],facecolor=(0.9,0.9,0.9))
x_dist, = ax1.plot([],[],'-b',linewidth = 2, label = 'X ='+str(a)+str('*t^')+str(b))
horizontal_line, = ax1.plot([],[],'r:o',linewidth = 2,label = 'horizontal line')
vertical_line, = ax1.plot([],[],'g:o',linewidth = 2, label = 'Vertical line')

# Subplot 2 properties
plt.xlim(t[0],t[-1])
plt.ylim(x[0],x[-1])
plt.xticks(np.arange(t[0],t[-1]+0.00001,t[-1]/4),size=10)
plt.yticks(np.arange(x[0],x[-1]+1,x[-1]/4),size=10)
plt.xlabel('Time',fontsize = 15)
plt.ylabel('Distance [km]',fontsize = 15)
plt.grid(True)
plt.legend(loc='upper left',fontsize='x-large')

# Creating Subplot 3
ax2 = fig.add_subplot(gs[1,1],facecolor=(0.9,0.9,0.9))
speed, = ax2.plot([],'-b', linewidth = 2, label = 'Speed over time')
vertical_ax2, = ax2.plot([],[],'g:o',linewidth = 2,label = 'vertical line')
divisor_line, = ax2.plot([0.1,0.35],[1000,1000],'k',linewidth=1)
text_numerator = ax2.text(0.1,1040,'',fontsize=20, color = 'r')
text_denominator = ax2.text(0.1,840,'',fontsize=20, color = 'g')
text_ans = ax2.text(0.2,2000,'',fontsize = 15, color = 'b')

# Subplot 3 Properties
plt.xlim(t[0],t[-1])
plt.ylim(0,speed_x[-1]*2)
plt.grid(True)
plt.xticks(np.arange(t[0],t[-1]+0.00001,t[-1]/4),size = 10)
plt.yticks(np.arange(0,speed_x[-1]*2+1,speed_x[-1]*2/4),size=10)
plt.xlabel('Time [hr]')
plt.ylabel('Speed [km/hr]')
plt. legend(loc = 'upper right', fontsize = 'x-large')

box_object = dict(boxstyle = 'circle',fc = (0.2,0.9,0.9), ec = 'g', lw = 5)
text_ax0 = ax0.text(1200,0.3,'',size = 10,color = 'g',bbox = box_object)

box_obj_1 = dict(boxstyle = 'square',fc = (0.7,0.9,0.9), ec = 'r', lw = 1)
text_x_value = ax0.text(650,0.2,'',size = 10, color = 'r', bbox = box_obj_1)

box_obj_2 = dict(boxstyle = 'square',fc = (0.7,0.9,0.9), ec = 'b', lw = 1)
text_y_value = ax0.text(650,0.6,'',size = 10, color = 'b', bbox = box_obj_2)

plane_ani=animation.FuncAnimation(fig,update_plot,frames=frame_amount,interval=20,repeat=True,blit=True)
plt.show()
