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

#plot simple pendulum motion in while loop
i = 1
#set framerate values
f = 100

'work out time steps needed for animation'
#set 
while i/f <= position[-1]:
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
    plt.pause(1/f)

    #increment by time step
    i += 1

plt.show()
