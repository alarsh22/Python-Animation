import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Time array
t0 = 0
t_end = 14
dt = 0.02
t = np.arange(t0,t_end+dt,dt)

f1 = 1/3
A1 = 20
Train_Blue = A1*np.sin(2*np.pi*f1*t)

f2 = 1/12
A2 = -5
Train_Red = A2*np.cos(2*np.pi*f2*t)

# Cars:
y_i = 14
delay_car_green = 6.5
car_green = y_i-(t-delay_car_green)**2
delay_car_purple = 2.5
car_purple = y_i-2*(t-delay_car_purple)

########################################## ANIMATION ############################
frame_amount = len(t)

def update_plot(num):
    X_Blue.set_data(t[0:num],Train_Blue[0:num])
    X_Red.set_data(t[0:num], Train_Red[0:num])

    Blue_Block.set_data([Train_Blue[num]-0.45,Train_Blue[num]+0.45],[4.5,4.5])
    Red_Block.set_data([Train_Red[num]-0.45,Train_Red[num]+0.45],[1.5,1.5])

    if t[num]>=delay_car_green:
        Green_Block.set_data([3.5,3.5],[car_green[num]-0.3,car_green[num]+0.3])
        Y_Green.set_data(t[int(delay_car_green/dt):num],car_green[int(delay_car_green/dt):num])
    else:
        Green_Block.set_data([3.5,3.5],[y_i-0.3,y_i+0.3])
        Y_Green2.set_data(t[0:num],y_i)

    if t[num]>=delay_car_purple:
        Purple_Block.set_data([-3.5,-3.5], [car_purple[num] - 0.3, car_purple[num] + 0.3])
        Y_Purple.set_data(t[int(delay_car_purple/dt):num], car_purple[int(delay_car_purple/dt):num])
    else:
        Purple_Block.set_data([-3.5,-3.5],[y_i-0.3,y_i+0.3])
        Y_Purple2.set_data(t[0:num],y_i)

    return X_Blue, X_Red, Blue_Block, Red_Block, Green_Block, Y_Green, Purple_Block, Y_Purple,Y_Purple2,Y_Green2

# Figure set up
fig = plt.figure(figsize=(16,9),dpi = 120, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(2,2)

# Top left subplot creation (TRAINS):
Ob1 = fig.add_subplot(gs[0,0], facecolor = (0.8,0.8,0.8))
X_Blue, = Ob1.plot([],[],'b',linewidth = 3, label = 'X Blue = '+str(A1)+'sin(2*pi*'+str(round(f1,2))+'*t)')
X_Red, = Ob1.plot([],[],'r', linewidth = 3, label = 'X Red = '+str(A2)+'cos(2*pi*'+str(round(f2,2))+'*t)')
plt.xlim(t0,t_end)
plt.ylim(-(A1+1),(A1+1))
plt.xlabel('Time [sec]')
plt.ylabel('X [m]')
Ob1.spines['bottom'].set_position('center')
Ob1.xaxis.set_label_coords(0.5,0)
plt.legend(bbox_to_anchor=(1,1.2),fontsize='medium')
copyright=Ob1.text(0,(y_i+10)*3.2/3,'© AL ARSH BASHEER',size=12)
plt.grid(True)

# Bottom Left Subplot (CARS):
Ob2 = fig.add_subplot(gs[1,0], facecolor = (0.8,0.8,0.8))
Y_Green, = Ob2.plot([],[],'g',linewidth = 3, label = 'Green Car')
Y_Green2, = Ob2.plot([],[],'g',linewidth = 3,alpha = 0.3)
Y_Purple, = Ob2.plot([],[],'m',linewidth = 5, label = 'Purple Car')
Y_Purple2, = Ob2.plot([],[],'m',linewidth = 5,alpha = 0.5)
plt.xlim(t0,t_end)
plt.ylim(-4,y_i+1)
plt.xlabel('Time [sec]')
plt.ylabel('Y [m]')
Ob2.spines['bottom'].set_position(('data',0))
Ob2.xaxis.set_label_coords(0.5,0)
plt.legend(loc = 'upper right')
plt.grid(True)

# Right side Subplot
Ob3 = fig.add_subplot(gs[:,1], facecolor = (0.8,0.8,0.8))
Blue_Block, = Ob3.plot([],[],'b',linewidth = 20)
Green_Block, = Ob3.plot([],[],'g',linewidth = 20)
Red_Block, = Ob3.plot([],[],'r',linewidth = 20)
Purple_Block, = Ob3.plot([],[],'m',linewidth = 20)

# Intersection Zones:
Intersection_zone_1 = Ob3.plot([3,4],[1,1],'-k',linewidth = 3)
Intersection_zone_12 = Ob3.plot([3,3],[1,2],'-k',linewidth = 3)
Intersection_zone_13 = Ob3.plot([3,4],[2,2],'-k',linewidth = 3)
Intersection_zone_14 = Ob3.plot([4,4],[1,2],'-k',linewidth = 3)

Intersection_zone_2 = Ob3.plot([3,4],[4,4],'-k',linewidth = 3)
Intersection_zone_22 = Ob3.plot([3,3],[4,5],'-k',linewidth = 3)
Intersection_zone_23 = Ob3.plot([3,4],[5,5],'-k',linewidth = 3)
Intersection_zone_24 = Ob3.plot([4,4],[4,5],'-k',linewidth = 3)

Intersection_zone_3 = Ob3.plot([-3,-4],[1,1],'-k',linewidth = 3)
Intersection_zone_32 = Ob3.plot([-3,-3],[1,2],'-k',linewidth = 3)
Intersection_zone_33 = Ob3.plot([-3,-4],[2,2],'-k',linewidth = 3)
Intersection_zone_34 = Ob3.plot([-4,-4],[1,2],'-k',linewidth = 3)

Intersection_zone_4 = Ob3.plot([-3,-4],[4,4],'-k',linewidth = 3)
Intersection_zone_42 = Ob3.plot([-3,-3],[4,5],'-k',linewidth = 3)
Intersection_zone_43 = Ob3.plot([-3,-4],[5,5],'-k',linewidth = 3)
Intersection_zone_44 = Ob3.plot([-4,-4],[4,5],'-k',linewidth = 3)

plt.xlim(-max(A1,A2)-1,max(A1,A2)+1)
plt.ylim(-2,y_i+1)
Ob3.spines['left'].set_position('center')
Ob3.spines['bottom'].set_position(('data',0))

plt.grid(True)


ANIMATION = animation.FuncAnimation(fig,update_plot,frames=frame_amount,interval=20,repeat=False,blit=True)
plt.show()