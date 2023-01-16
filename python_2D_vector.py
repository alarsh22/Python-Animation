import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np
type =3
# Create time array:

t0 = 0
t_end = 10
dt = 0.02
t = np.arange(t0,t_end+dt,dt)

if type==1:
    #Create x-axis:
    x_i = 1000
    a = 200
    x = a*t + x_i

    #Create y-axis:
    y_i = 1500
    b = -100
    y = y_i + b*t

elif type==2:
    # Create x-axis:
    x_i = 1000
    a = 200
    x = a*t**2 + x_i

    # Create y-axis:
    y_i = 1500
    A=500
    f = 0.1
    y = A*np.sin(2*np.pi*f*t) +y_i
else:
    r = 40
    f = 1
    a = 1000+ 5*t
    b = 500 + 40*t
    x = (1000 + t)+r*np.cos(2*np.pi*f*t)
    y = (500 + 90*t)+r*np.sin(2*np.pi*f*t)

############################ ANIMATION ################################

frame_amount = len(t)

def update_plot(num):
    Airplane.set_data([x[num]-15,x[num]+15],[y[num],y[num]])
    plane_trajectory.set_data(x[0:num],y[0:num])
    X_trajectory.set_data(t[0:num],x[0:num])
    Y_trajectory.set_data(t[0:num],y[0:num])
    if type!=3:
        arrow = Ob1.arrow(0,0,x_i,y_i,length_includes_head=True,head_width=40,head_length = 80,color='g',linewidth=2)
        moving_arrow = Ob1.arrow(0,0,x[num],y[num],length_includes_head=True,head_width=40,head_length=80,color='r',linewidth=2)
        displacement_arrow = Ob1.arrow(x_i,y_i,x[num]-x_i,y[num]-y_i,length_includes_head = True,head_width=40,head_length=80,color='b',linewidth=2)
        x_component_arrow = Ob1.arrow(x_i,y_i,x[num]-x_i,0,length_includes_head = True,head_width=40,head_length=80,color='r',linewidth=2)
        y_component_arrow = Ob1.arrow(x[num],y_i,0,y[num]-y_i,length_includes_head = True,head_width=40,head_length=80,color='b',linewidth=2)
        leftplot_arrow = Ob2.arrow(t[num],x_i,0,x[num]-x_i,length_includes_head = True,head_width=0.2,head_length = 80,color='b',linewidth = 2)
        right_arrow = Ob3.arrow(t[num],y_i,0,y[num]-y_i,length_includes_head = True,head_width=0.2,head_length = 80,color='r',linewidth = 2)
        return Airplane, plane_trajectory,X_trajectory,Y_trajectory,arrow, moving_arrow,displacement_arrow,x_component_arrow,y_component_arrow,leftplot_arrow,right_arrow
    else:
        r_displacement_arrow = Ob1.arrow(a[num], b[num], x[num] - a[num], y[num] - b[num], length_includes_head=True, head_width=40,head_length=80, color='b', linewidth=2)
        r_x_component_arrow = Ob1.arrow(a[num], b[num], x[num] - a[num], 0, length_includes_head=True, head_width=40, head_length=80,color='r', linewidth=2)
        r_y_component_arrow = Ob1.arrow(x[num], b[num], 0, y[num] - b[num], length_includes_head=True, head_width=40, head_length=80,color='b', linewidth=2)
        r_leftplot_arrow = Ob2.arrow(t[num],0, 0, x[num], length_includes_head=True, head_width=0.2, head_length=80,color='b', linewidth=2)
        r_right_arrow = Ob3.arrow(t[num], b[num], 0, y[num] - b[num], length_includes_head=True, head_width=0.2, head_length=80,color='r', linewidth=2)
        return Airplane, plane_trajectory, X_trajectory, Y_trajectory, r_displacement_arrow, r_x_component_arrow, r_y_component_arrow, r_leftplot_arrow, r_right_arrow


fig = plt.figure(figsize=(16,9),dpi = 120, facecolor=(0.9,0.9,0.9))
gs = gridspec.GridSpec(2,2)

Ob1 = fig.add_subplot(gs[0,:],facecolor=(0.9,0.9,0.9))
Airplane, = Ob1.plot([],[],'k', linewidth = 7)
plane_trajectory, = Ob1.plot([],[],'--k', linewidth = 2)

if type==3:
    plt.xlim(0,2000)
    plt.ylim(150,3000)
else:
    plt.xlim(0,max(x)+100)
    plt.ylim(0,max(y)+100)
plt.xlabel('Distance travelled [km]')
plt.ylabel('Altitude [m]')
plt.grid(True)

# Second Subplot:
Ob2 = fig.add_subplot(gs[1,0], facecolor = (0.9,0.9,0.9))
if type==1:
    X_trajectory, = Ob2.plot([],[],'-r', linewidth = 2, label = 'x = 200*t + '+str(x_i))
elif type==2:
    X_trajectory, = Ob2.plot([],[],'-r', linewidth = 2, label = 'x = 200*t^2 + '+str(x_i))
else:
    X_trajectory, = Ob2.plot([],[],'-r', linewidth = 2, label = 'x = a + r(t)*cos(2*pi*f(t)*t)')

if type==3:
    plt.xlim(t0,t_end)
    plt.ylim(800,2000)

else:
    plt.xlim(0,max(t))
    plt.ylim(0,max(x))
plt.xlabel('Time [s]')
plt.ylabel('Position x [m]  ')
plt.legend(loc = 'lower right')
plt.grid(True)

#Third Subplot
Ob3 = fig.add_subplot(gs[1,1],facecolor = (0.9,0.9,0.9))
if type==1:
    Y_trajectory, = Ob3.plot([],[],'-g',linewidth = 2, label = 'y = -100*t +'+ str(y_i))
elif type==2:
    Y_trajectory, = Ob3.plot([],[],'-g',linewidth = 2, label = 'y = '+str(A)+'sin(2*pi*'+str(f)+'*t) + '+str(y_i))
else:
    Y_trajectory, = Ob3.plot([],[],'-g',linewidth = 2, label = 'y = b + r(t)*sin(2*pi*f(t)*t)')

if type==3:
    plt.xlim(t0,t_end)
    plt.ylim(0,1500)
else:
    plt.xlim(0,max(t))
    plt.ylim(0,max(y))
plt.xlabel('Time [s]')
plt.ylabel('Altitude [m]')
plt.legend(loc = 'upper right')
plt.grid(True)

ANI = animation.FuncAnimation(fig,update_plot,frames=frame_amount,interval=20,repeat=True,blit=True)
plt.show()
