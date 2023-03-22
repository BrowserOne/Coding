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

#setup variable for a pendulum object
ob = pd(0.1, 10.0,theta = 90, setstep = 'Runge-kuttaSimple')

#define time duration of simulation run and time step between each iteration
t_max = 10     #[s]
dt = 1/100      #[s]

#assign list for position data
omega = []
theta = []
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

    # calculate kinetic energy
    KE = (1/2)*ob._M*(ob._L*ob._omega)**2

    # calculate potential energy
    PE = ob._M*ob._g*(ob.y()+ob._L)

    # calculate total energy
    E = KE + PE

    # add energy values to list
    ke.append(KE)
    pe.append(PE)
    e .append( E)

    #save energy data to readable file
    pk.dump(ke, open("Kenergy","wb"))
    pk.dump(pe, open("Penergy","wb"))
    pk.dump(e , open( "energy","wb"))

    #plot motion and energy values
    # plt.cla()
    # ax2.cla()
    # plt.plot(ob.x(),ob.y(), 'ro')
    # plt.plot([0,ob.x()], [0,ob.y()], '-r')
    # plt.xlim([(-ob._L)-ob._L/5, (ob._L)+ob._L/5])  
    # plt.ylim([(-ob._L)-ob._L/5,(ob._L)+ob._L/5])
    # plt.xlabel('x [m]')
    # plt.ylabel('y [m]')
    # plt.title("t={:0.1f}".format(ob._t))
    # ax2.plot(0, KE, 'ro')
    # ax2.plot(0, PE, 'bo')
    # ax2.plot(0, E , 'go')
    # ax2._xlim(-1,1)
    # ax2._ylim(-10,50)
    # plt.pause(0.01)


