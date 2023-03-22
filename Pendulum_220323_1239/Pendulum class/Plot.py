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