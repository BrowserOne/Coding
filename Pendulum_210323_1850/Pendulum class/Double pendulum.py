"""
This program used to run a simulation of a double pendulum system. 
It uses the pendulum class in the Setup file to define two pendulum objects and uses the step function from the pendulum class to iterate the motion of the pendulum.
It iterates time in defied steps that vary with the motion of the object until a defined max time.
It can be used to animate the motion of the pendulum or used to print the energy and momentum of the system to test conservation.

Author: Sreecharan Chakrala
Date:21/03/2023
Email:S.chakrala@lancaster.ac.uk
"""

#import class used to define a pendulum object
from Setup import pendulum as pd

# import required modules
import matplotlib.pyplot as plt
import numpy as np

#setup variable for two objects in the format of a list
ob = pd(np.array([1.0,1.0]), np.array([10,5]),theta = np.array([170,90]), omega = np.array([0.0,0.0]), setstep = 'Runge-KuttaDouble')

#define time duration of simulation run and time step between each iteration
t_max = 10          #[s]
DT = 1/1000         #[s]

#calculate total length of two pendulum system
L = ob._L[0] + ob._L[1]     #[m]

# fig, (ax1, ax2) = plt.subplots(1, 2)

#assign list for energy data
ke = []
pe = []
e = []

#assign list for momentum data
P1 = []
P2 = []
P = []

#set up loop to iterate motion
while ob._t<t_max:

    #set variable time step based on motion of the pendulum. condition to account for zero velocity.
    if ob._omega[0]**2 + ob._omega[1]**2 == 0.0:
        dt = DT
    else:
        dt = DT/np.sqrt(ob._omega[0]**2 + ob._omega[1]**2)

    #increment motion with time step dt
    ob.step(dt)

    #calculate second pendulum position in relation to first pendulum
    x2 = ob.x()[0] + ob.x()[1]
    y2 = ob.y()[0] + ob.y()[1]

    #Kinetic energy
    KE = (1/2)*(ob._M[0])*(ob._L[0]*ob._omega[0])**2 + (1/2)*(ob._M[1])*((ob._L[0]*ob._omega[0])**2 +
                                                                          (ob._L[1]*ob._omega[1])**2 +
                                                                            (2*ob._L[0]*ob._L[1]*ob._omega[0]*ob._omega[1]*np.cos(ob._theta[0] - ob._theta[1])))

    #Potential energy
    PE = ob._M[0]*ob._g*(ob._L[0]+ob._L[1]-ob._L[0]*np.cos(ob._theta[0]))  + ob._M[1]*ob._g*(ob._L[0] + ob._L[1] - (ob._L[0]*np.cos(ob._theta[0]) + ob._L[1]*np.cos(ob._theta[1]))) 

    #total energy
    E = KE + PE     

    #add energy values to list
    ke.append(KE)
    pe.append(PE)
    e .append( E)

    #calculate momentum of pendulum system
    # p1 = ob._M[0]*ob._L[0]**2*(2*ob._omega[0] + ob._omega[1]*np.cos(ob._theta[0] - ob._theta[1]))
    # p2 = ob._M[1]*ob._L[1]**2*(ob._omega[1] + ob._omega[0]*np.cos(ob._theta[0] - ob._theta[1]))

    #total momentum
    # p = p1 + p2

    #add momentum values to list
    # P1.append(p1)
    # P2.append(p2)
    # P.append(p)
    
    # if ob._t % 1/1000 == 0:

    #plot data
#     plt.cla()
# #     # ax2.cla()
#     plt.plot(ob.x()[0],ob.y()[0], 'bo')
#     plt.plot([0,ob.x()[0]], [0,ob.y()[0]], '-b')
#     plt.plot(x2,y2,'ro')
#     plt.plot([ob.x()[0],x2],[ob.y()[0],y2], '-r')
#     plt.xlim([(-L)-L/5, (L)+L/5])  
#     plt.ylim([(-L)-L/5, (L)+L/5])
#     plt.xlabel('x [m]')
#     plt.ylabel('y [m]')
#     plt.title("t={:0.1f}".format(ob._t))
# #     # ax2.plot(0, KE, 'ro')
# #     # ax2.plot(0, PE, 'bo')
# #     # ax2.plot(0, E , 'go')
# #     # ax2.set_xlim(-1,1)
# #     # ax2.set_ylim(-10,250)
#     plt.pause(0.0001)
#     # print(ob._t)

#plot energy
plt.plot(ke, label = 'KE')
plt.plot(pe, label = 'PE')
plt.plot(e , label = 'E')

#plot momentum
# plt.plot(P1, label = 'P1')
# plt.plot(P2, label = 'P2')
# plt.plot(P, label = 'P')

plt.legend()


plt.show()
