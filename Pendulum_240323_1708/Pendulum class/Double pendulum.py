"""
This program used to run a simulation of a double pendulum system. 
It uses the pendulum class in the Setup file to define two pendulum objects and uses the step function from the pendulum class to iterate the motion of the pendulum.
It iterates time in defied steps that vary with the motion of the object until a defined max time.
The data is then saved on a file that can be read by the Plot script in order to animation motion of the pendulum.

Author: Sreecharan Chakrala
Date:21/03/2023
Email:S.chakrala@lancaster.ac.uk
"""

#import class used to define a pendulum object
from Setup import pendulum as pd

# import required modules
import pickle as pk
import numpy as np
import time
import matplotlib.pyplot as plt

#check start time to time how long the script took to run
start_time = time.time()

#setup variable for two objects in the format of a list
ob = pd(np.array([1.0,1.0]), np.array([10,5]), theta = np.array([170,90]), omega = np.array([0.0,0.0]), setstep = 'Runge-KuttaDouble')

#define time duration for simulation and time step between each iteration
t_max = 10          #[s]
DT = 1/1000         #[s]

#calculate total length of two pendulum system
L = ob._L[0] + ob._L[1]     #[m]

#assign list for energy data
ke = []
pe = []
e = []

#assign list for momentum data
P1 = []
P2 = []
P = []

#  #set variable to test number of errors in calculation of motion
i = 0

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

  i += ob.valid()

  #calculate momentum of pendulum system
  # p1 = ob._M[0]*ob._L[0]**2*(2*ob._omega[0] + ob._omega[1]*np.cos(ob._theta[0] - ob._theta[1]))
  # p2 = ob._M[1]*ob._L[1]**2*(ob._omega[1] + ob._omega[0]*np.cos(ob._theta[0] - ob._theta[1]))

  #total momentum
  # p = p1 + p2

  #add momentum values to list
  # P1.append(p1)
  # P2.append(p2)
  # P.append(p)
    

  # #plot data
  # plt.cla()
  # plt.plot(ob.x()[0],ob.y()[0], 'bo')
  # plt.plot([0,ob.x()[0]], [0,ob.y()[0]], '-b')
  # plt.plot(x2,y2,'ro')
  # plt.plot([ob.x()[0],x2],[ob.y()[0],y2], '-r')
  # plt.xlim([(-L)-L/5, (L)+L/5])  
  # plt.ylim([(-L)-L/5, (L)+L/5])
  # plt.xlabel('x [m]')
  # plt.ylabel('y [m]')
  # plt.title("t={:0.1f}".format(ob._t))
  # plt.pause(0.0001)
  # # print(ob._t)

#save energy data to readable file
pk.dump(ke, open("Kenergy","wb"))
pk.dump(pe, open("Penergy","wb"))
pk.dump(e , open( "energy","wb"))

#test validity of motion of pendulum
if i == 0:
  print('Congratulations you didn\'t mess up')
else:
  print('You have messed up {} times'.format(i))

#print a conformation that the code as completed and duration of run time
print("Calculation completed in {:0.001f}s".format(time.time() - start_time))


'limitations also for very small lengths of second pendulum as it would make the angular momentum very very large'