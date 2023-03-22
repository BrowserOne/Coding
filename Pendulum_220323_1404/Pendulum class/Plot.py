"""
This scrypt is created as the last step in the simulation of the pendulum to make the computation of calculating the steps of the simulation and the computation to plot separate.
"""

#import required modules
import matplotlib.pyplot as plt
import pickle as pk

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
i = 0.0

while i<= position[-1]:

    #plot current position data of pendulum
    plt.cla()
    plt.plot(position[i][0],position[i][1], 'ro')
    plt.plot([0,position[i][0]], [0,position[i][1]], '-r')
    plt.xlim([(-position[i][-2])-position[i][-2]/5, (position[i][-2])+position[i][-2]/5])  
    plt.ylim([(-position[i][-2])-position[i][-2]/5,(position[i][-2])+position[i][-2]/5])
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.title("t={:0.1f}".format(position[i][2]))

    #increment by time step
    i += position[-3]

plt.show()
