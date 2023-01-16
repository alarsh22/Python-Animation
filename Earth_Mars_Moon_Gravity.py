import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Time array
t0 = 0
t_end = 12
dt = 0.02
t = np.arange(t0,t_end+dt,dt)

# Gravitational acceleration
g_Earth = -9.8 # (m/s^2)
g_Mars = -3.721
g_Moon = g_Earth/6



n = 2
y_i = 100 # [m]
y_Earth = y_i + 0.5*g_Earth*t**n
y_Mars = y_i + 0.5*g_Mars*t**n
y_Moon = y_i + 0.5*g_Moon*t**n
# print(y_Earth)

# Velocities

y_Earth_velocity = 0.5*n*g_Earth*t**(n-1)
y_Mars_velocity = 0.5*n*g_Mars*t**(n-1)
y_Moon_velocity = 0.5*n*g_Moon*t**(n-1)

# Acceleration

y_Earth_acceleration = 0.5*n*(n-1)*g_Earth*t**((n-1)-1)
y_Mars_acceleration = 0.5*n*(n-1)*g_Mars*t**((n-1)-1)
y_Moon_acceleration = 0.5*n*(n-1)*g_Moon*t**((n-1)-1)

# Make circle

def make_circle(r):
    degree = np.arange(0,361,1)
    radian = (np.pi*degree)/180
    ball_x = r*np.cos(radian)
    ball_y = r*np.sin(radian)
    return ball_x,ball_y

radius = 5
ball_x_Earth, ball_y_Earth = make_circle(radius)
ball_x_Mars, ball_y_Mars = make_circle(radius)
ball_x_Moon, ball_y_Moon = make_circle(radius)

#np.set_printoptions(suppress= True)
#print(ball_x_Earth)
#print(ball_y_Earth)
##################################### ANIMATION ###########################
frame_amount = len(t)
width = 1.2
y_bottom = -10 #[m]
dy = 10

def update_plot(num):
    if y_Earth[num]>radius:
        ball_Earth.set_data(ball_x_Earth,ball_y_Earth+y_Earth[num])
        Position_Earth.set_data(t[0:num],y_Earth[0:num])
        Velocity_Earth.set_data(t[0:num], y_Earth_velocity[0:num])
        Acceleration_Earth.set_data(t[0:num], y_Earth_acceleration[0:num])
    if y_Mars[num]>radius:
        ball_Mars.set_data(ball_x_Mars,ball_y_Mars+y_Mars[num])
        Position_Mars.set_data(t[0:num],y_Mars[0:num])
        Velocity_Mars.set_data(t[0:num], y_Mars_velocity[0:num])
        Acceleration_Mars.set_data(t[0:num], y_Mars_acceleration[0:num])

    if y_Moon[num]>radius:
        ball_Moon.set_data(ball_x_Moon,ball_y_Moon+y_Moon[num])
        Position_Moon.set_data(t[0:num], y_Moon[0:num])
        Velocity_Moon.set_data(t[0:num], y_Moon_velocity[0:num])
        Acceleration_Moon.set_data(t[0:num], y_Moon_acceleration[0:num])

    return ball_Earth, ball_Mars, ball_Moon, Position_Earth, Velocity_Earth, Acceleration_Earth, Position_Mars, Velocity_Mars, Acceleration_Mars, Position_Moon, Velocity_Moon, Acceleration_Moon

# Figure Properties
fig = plt.figure(figsize=(16,9),dpi = 120, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(3,4)

# Create Object for Earth
Ob1 = fig.add_subplot(gs[:,0],facecolor=(0.7,0.7,0.7))
ball_Earth,=Ob1.plot([],[],'k',linewidth=3)
ground_Earth,=Ob1.plot([-radius*width,radius*width],[-5,-5],linewidth = 38)
plt.xlim(-radius*width,radius*width)
plt.ylim(y_bottom,y_i+dy)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(y_bottom,y_i+2*dy,dy))
plt.ylabel('Altitude [m]')
plt.xlabel('Raidus')
plt.title('Earth')
copyright=Ob1.text(-radius*width,(y_i+10)*3.2/3,'© AL ARSH BASHEER',size=12)
# Create Object for Mars:
Ob2 = fig.add_subplot(gs[:,1],facecolor=(0.7,0.7,0.7))
ball_Mars,=Ob2.plot([],[],'k',linewidth=3)
ground_Mars,=Ob2.plot([-radius*width,radius*width],[-5,-5],'orangered',linewidth = 38)
plt.xlim(-radius*width,radius*width)
plt.ylim(y_bottom,y_i+dy)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(y_bottom,y_i+2*dy,dy))
plt.xlabel('Raidus')
plt.title('Mars')

# Create Object for Moon:
Ob3 = fig.add_subplot(gs[:,2],facecolor=(0.7,0.7,0.7))
ball_Moon,=Ob3.plot([],[],'k',linewidth=3)
ground_Moon,=Ob3.plot([-radius*width,radius*width],[-5,-5],'gray',linewidth = 38)
plt.xlim(-radius*width,radius*width)
plt.ylim(y_bottom,y_i+dy)
plt.xticks(np.arange(-radius,radius+1,radius))
plt.yticks(np.arange(y_bottom,y_i+2*dy,dy))
plt.xlabel('Raidus')
plt.title('Moon')

# Position function
Ob4 = fig.add_subplot(gs[0,3],facecolor = (0.9,0.9,0.9))

Position_Earth, = Ob4.plot([],[],'',linewidth=3,label='Altitude Earth')
Position_Mars, = Ob4.plot([],[],'orangered',linewidth=3,label='Altitude Mars')
Position_Moon, = Ob4.plot([],[],'gray',linewidth=3,label='Altitude Moon')

plt.xlim(0,t_end)
plt.ylim(0,y_i)
plt.legend(loc = (0.6,0.7),fontsize='x-small')
plt.ylabel('Altitude [m]')
Ob4.yaxis.set_label_coords(1.1,0.5)
plt.grid(True)



# Velocity function
Ob5 = fig.add_subplot(gs[1,3], facecolor = (0.9,0.9,0.9))

Velocity_Earth, = Ob5.plot([],[],'',linewidth=3,label='Velocity Earth')
Velocity_Mars, = Ob5.plot([],[],'orangered',linewidth=3,label='Velocity Mars')
Velocity_Moon, = Ob5.plot([],[],'gray',linewidth=3,label='Velocity Moon')

plt.xlim(0,t_end)
plt.ylim(y_Earth_velocity[-1],0)
plt.legend(loc = 'lower right',fontsize='x-small')
plt.ylabel('Velocity [m/s]')
Ob5.yaxis.set_label_coords(1.1,0.5)
plt.grid(True)

# Acceleration function
Ob6 = fig.add_subplot(gs[2,3], facecolor = (0.9,0.9,0.9))

Acceleration_Earth, = Ob6.plot([],[],'',linewidth = 3, label = 'Acceleration Earth')
Acceleration_Mars, = Ob6.plot([],[],'orangered',linewidth = 3, label = 'Acceleration Mars')
Acceleration_Moon, = Ob6.plot([],[],'grey',linewidth = 3, label = 'Acceleration Moon')

plt.xlim(0,t_end)
plt.ylim(g_Earth-1,0)
plt.legend(loc = 'lower right', fontsize = 'x-small')
plt.ylabel('Acceleration [m/s^2]')
Ob6.yaxis.set_label_coords(1.1,0.5)
plt.grid(True)

ANIMATION = animation.FuncAnimation(fig,update_plot,frames=frame_amount,interval=20,repeat=True,blit=True)
plt.show()



