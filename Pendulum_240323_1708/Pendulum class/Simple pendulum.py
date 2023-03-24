"""
This program used to run a simulation of a pendulum system. 
It uses the pendulum class in the Setup file to define a pendulum object and uses the step function from the pendulum class to iterate the motion of the pendulum.
It iterates time in defied steps until a defined max time.
The data is then saved on a file that can be read by the Plot script in order to animation motion of the pendulum.

Author: Sreecharan Chakrala
Date:21/03/2023
Email:S.chakrala@lancaster.ac.uk
"""

#import class used to define a pendulum object
from Setup import pendulum as pd

# import required modules
import pickle as pk
import time
import numpy as np

#set start time to time time taken for processing process
start_time = time.time()

#setup variable for a pendulum object
ob = pd(0.1, 10.0, theta = 90, setstep = 'Runge-kuttaSimple')

#define time duration of simulation run and time step between each iteration
t_max = 10      #[s]
dt = 1/10000      #[s]

#save position date of pendulum
position = []
x = []
y = []
t = []

#assign list for energy data
ke = []
pe = []
e = []

# fig, (plt, ax2) = plt.subplots(1, 2)

#set up loop
while ob._t<t_max:
    #increment position of pendulum with time step dt
    ob.step(dt)

    #save motion of pendulum
    x.append(ob.x())
    y.append(ob.y())
    t.append(ob._t)

    # calculate kinetic energy
    KE = (1/2)*ob._M*(ob._L*ob._omega)**2

    # calculate potential energy
    PE = ob._M*ob._g*(ob.y()+ob._L)

    # calculate total energy
    E = KE + PE

    # add energy values to list
    ke.append(KE)
    pe.append(PE)
    e.append( E)

#add step, time and length data to motion of pendulum
position.append(x)
position.append(y)
position.append(t)
position.append(dt)
position.append(ob._L)
position.append(t_max)

#save position date to readable file
pk.dump(position, open("simple position","wb"))

#save energy data to readable file
pk.dump(ke, open("Kenergy","wb"))
pk.dump(pe, open("Penergy","wb"))
pk.dump(e , open( "energy","wb"))

#print completion statement to confirm completion of calculation
print("Calculation completed in {:0.001f}s".format(time.time() - start_time ))

