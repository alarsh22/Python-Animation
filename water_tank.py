import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Time array
t0 = 0
t_end = 60
dt = 0.04
t = np.arange(t0,t_end+dt,dt)

Vol_Tank_1 = np.zeros(len(t))
Vol_Tank_2 = np.zeros(len(t))
Vol_Tank_3 = np.zeros(len(t))

for i in range(0,len(t)):
    # Tank-1
    if t[i]<=22.5:
        Vol_Tank_1[i] = 50 + 2*t[i]
    elif t[i]<=32.5:
        Vol_Tank_1[i] = 95
        temp11 = i
    elif t[i]<=32.5 + 45**0.5:
        Vol_Tank_1[i] = 95 - (t[i] - t[temp11])**2
        temp12 = i
    elif t[i]<=42.5 + (45)**0.5:
        Vol_Tank_1[i] = 50 + np.sin(2*np.pi*(t[i]-t[temp12]))
    else:
        Vol_Tank_1[i] = 50

    # Tank-2
    if t[i]<=27.5:
        Vol_Tank_2[i] = 40 + 2*t[i]
    elif t[i]<=32.5:
        Vol_Tank_2[i] = 95
        temp21 = i
    elif t[i]<=32.5 + (45)**0.5:
        Vol_Tank_2[i] = 95 - (t[i] - t[temp21])**2
        temp22 = i
    elif t[i]<=37.5 + (45)**0.5:
        Vol_Tank_2[i] = 50 + 3*np.sin(2*np.pi*(t[i]-t[temp22]))
        temp23 = i
    elif t[i]<=42.5 + (45)**0.5:
        Vol_Tank_2[i] = 50 + np.sin(2*2*np.pi*(t[i]-t[temp23]))
    else:
        Vol_Tank_2[i] = 50

    # Tank-3
    if t[i]<=32.5:
        Vol_Tank_3[i] = 30 + 2*t[i]
    elif t[i]<=32.5 + 45**0.5:
        Vol_Tank_3[i] = 95 - (t[i] - 32.5)**2
        temp31 = i
    elif t[i]<=42.5 + (45)**0.5:
        Vol_Tank_3[i] = 50 + (-1)*np.sin(2*np.pi*(t[i]-t[temp31]))
    else:
        Vol_Tank_3[i] = 50

######################################## ANIMATION ################################
frame_amount = len(t)

# Creating water tanks:
radius = 5 # [m]
vol_i = 0 # [m^3]
vol_f = 100
d_vol = 10

def update_plot(num):
    tank_level.set_data([-radius,radius],[Vol_Tank_1[num],Vol_Tank_1[num]])
    tank_fluid.set_data([0,0],[-64,Vol_Tank_1[num]-68])
    Tank1.set_data(t[0:num],Vol_Tank_1[0:num])
    Tank1P2.set_data(t[0:num],Vol_Tank_1[0:num])

    tank_level2.set_data([-radius,radius],[Vol_Tank_2[num],Vol_Tank_2[num]])
    tank_fluid2.set_data([0,0],[-64,Vol_Tank_2[num]-68])
    Tank2.set_data(t[0:num],Vol_Tank_2[0:num])
    Tank2P2.set_data(t[0:num],Vol_Tank_2[0:num])

    tank_level3.set_data([-radius,radius],[Vol_Tank_3[num],Vol_Tank_3[num]])
    tank_fluid3.set_data([0,0],[-64,Vol_Tank_3[num]-68])
    Tank3.set_data(t[0:num],Vol_Tank_3[0:num])
    Tank3P2.set_data(t[0:num],Vol_Tank_3[0:num])

    return tank_level, tank_fluid, Tank1, tank_level2, tank_fluid2, Tank2, tank_level3, tank_fluid3, Tank3,Tank1P2,Tank2P2,Tank3P2

fig = plt.figure(figsize=(16,9),dpi = 120, facecolor=(0.8,0.8,0.8))
gs = gridspec.GridSpec(2,3)

# Creating Tank-1:
Ob1 = fig.add_subplot(gs[0,0],facecolor = (0.9,0.9,0.9))
tank_level, = Ob1.plot([],[],'k',linewidth = 4)
tank_fluid, = Ob1.plot([],[],'royalblue', linewidth = 260)
plt.ylabel('Tank Volume [m^3]')
plt.xlim(-radius,radius)
plt.ylim(vol_i,vol_f)
plt.title('Tank-1')
plt.grid(True)

copyright=Ob1.text(-5,(vol_f+10)*3.2/3,'© AL ARSH BASHEER',size=12)


# Creating Tank-2:
Ob2 = fig.add_subplot(gs[0,1],facecolor = (0.9,0.9,0.9))
tank_level2, = Ob2.plot([],[],'k',linewidth = 4)
tank_fluid2, = Ob2.plot([],[],'royalblue', linewidth = 260)
plt.xlim(-radius,radius)
plt.ylim(vol_i,vol_f)
plt.title('Tank-2')
plt.grid(True)

# Creating Tank-3:
Ob3 = fig.add_subplot(gs[0,2],facecolor = (0.9,0.9,0.9))
tank_level3, = Ob3.plot([],[],'k',linewidth = 4)
tank_fluid3, = Ob3.plot([],[],'royalblue', linewidth = 260)
plt.xlim(-radius,radius)
plt.ylim(vol_i,vol_f)
plt.title('Tank-3')
plt.grid(True)

# Volume Plot
Ob4 = fig.add_subplot(gs[1,0:2],facecolor = (0.9,0.9,0.9))
Tank1, = Ob4.plot([],[],'blue', linewidth = 3, label = 'Tank-1')
Tank2, = Ob4.plot([],[],'green', linewidth = 3, label = 'Tank-2')
Tank3, = Ob4.plot([],[],'red', linewidth = 3, label = 'Tank-3')
plt.xlim(t0,t_end)
plt.ylim(vol_i,vol_f)
plt.title('Tank-3')
plt.legend(loc = 'upper right')
plt.grid(True)

# Right side plot:
Ob5 = fig.add_subplot(gs[1,2], facecolor = (0.9,0.9,0.9))
Tank1P2, = Ob5.plot([],[],'blue', linewidth = 3, label = 'Tank-1')
Tank2P2, = Ob5.plot([],[],'green', linewidth = 3, label = 'Tank-2')
Tank3P2, = Ob5.plot([],[],'red', linewidth = 3, label = 'Tank-3')
plt.axis([37,50,46,54])
plt.title('Tank-3')
plt.legend(loc='upper right')
plt.grid(True)

ANIMATION = animation.FuncAnimation(fig,update_plot,frames=frame_amount,interval=20,repeat=True,blit=True)
plt.show()