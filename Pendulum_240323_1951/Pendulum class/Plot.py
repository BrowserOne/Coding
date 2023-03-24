"""
This scrypt is created as the last step in the simulation of the pendulum to make the computation of calculating the steps of the simulation and the computation to plot separate.
"""

#import required modules
import matplotlib.pyplot as plt
import pickle as pk
from scipy.interpolate import interp1d

#load energy data one variable
kinetic = pk.load(open("Kenergy", "rb"))
potential = pk.load(open("Penergy", "rb"))
energy = pk.load(open("energy", "rb"))

#plot energy data to test energy conservation through motion of pendulum
plt.plot(kinetic, label = 'KE')
plt.plot(potential, label = 'PE')
plt.plot(energy , label = 'E')
plt.legend()

plt.show()

#load motion of pendulum
position = pk.load(open("simple position","rb"))

def plot_simple():
    #set up an interpolation for x and y values
    x_f = interp1d(position[2],position[0],'linear')
    y_f = interp1d(position[2],position[1],'linear')

    #plot current position data of pendulum
    plt.cla()
    plt.plot(x_f(i/f),y_f(i/f), 'ro')
    plt.plot([0,x_f(i/f)], [0,y_f(i/f)], '-r')
    plt.xlim([(-position[-2])-position[-2]/5, (position[-2])+position[-2]/5])  
    plt.ylim([(-position[-2])-position[-2]/5,(position[-2])+position[-2]/5])
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.title("t={:0.1f}".format(i/f))
    plt.pause(1/f**2)

def plot_double():
    #set up an interpolation for x and y values
    x1_f = interp1d(position[4],position[0],'linear')
    x2_f = interp1d(position[4],position[1],'linear')
    y1_f = interp1d(position[4],position[2],'linear')
    y2_f = interp1d(position[4],position[3],'linear')

    #plot current position data of pendulum
    plt.cla()
    plt.plot(x1_f(i/f),y1_f(i/f), 'bo')
    plt.plot([0,x1_f(i/f)], [0,y1_f(i/f)], '-b')
    plt.plot(x2_f(i/f),y2_f(i/f), 'ro')
    plt.plot([x1_f(i/f),x2_f(i/f)], [y1_f(i/f),y2_f(i/f)], '-r')
    plt.xlim([(-position[-2])-position[-2]/5, (position[-2])+position[-2]/5])  
    plt.ylim([(-position[-2])-position[-2]/5,(position[-2])+position[-2]/5])
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.title("t={:0.1f}".format(i/f))
    plt.pause(0.001)
'work out time steps needed for animation'
#plot simple pendulum motion in while loop
i = 1
#set framerate values
f = 200

#set while loop
while i/f <= position[-1]:
    plot_double()
    #increment by time step
    i += 1

plt.show()
