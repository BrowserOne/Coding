from Setup import pendulum as pd
import matplotlib.pyplot as plt
import numpy as np

ob = pd(np.array([1.0,1.0]), np.array([10,5]),theta = np.array([170,90]), omega = np.array([0.0,0.0]), setstep = 'Runge-KuttaDouble')
t_max = 10  #[s]
DT = 1/1000   #[s]
L = ob._L[0] + ob._L[1]

# fig, (ax1, ax2) = plt.subplots(1, 2)
ke = []
pe = []
e = []

P1 = []
P2 = []
P = []
#set up loop
while ob._t<t_max:
    if ob._omega[0]**2 + ob._omega[1]**2 == 0.0:
        dt = DT
    else:
        dt = DT/np.sqrt(ob._omega[0]**2 + ob._omega[1]**2)

    #increment velcoity account for angle being 0.0
    ob.step(dt)
    x2 = ob.x()[0] + ob.x()[1]
    y2 = ob.y()[0] + ob.y()[1]

    #calculate energy and momenutm for position
    KE = (1/2)*(ob._M[0])*(ob._L[0]*ob._omega[0])**2 + (1/2)*(ob._M[1])*((ob._L[0]*ob._omega[0])**2 +
                                                                          (ob._L[1]*ob._omega[1])**2 +
                                                                            (2*ob._L[0]*ob._L[1]*ob._omega[0]*ob._omega[1]*np.cos(ob._theta[0] - ob._theta[1])))  #Kinetic energy

    PE = ob._M[0]*ob._g*(ob._L[0]+ob._L[1]-ob._L[0]*np.cos(ob._theta[0]))  + ob._M[1]*ob._g*(ob._L[0] + ob._L[1] - (ob._L[0]*np.cos(ob._theta[0]) + ob._L[1]*np.cos(ob._theta[1])))  - ob._M[0]*ob._g*ob._L[1] #Potential energy

    E = KE + PE                                                                                     #total energy
    ke.append(KE)
    pe.append(PE)
    e .append( E)
    # p1 = ob._M[0]*ob._L[0]**2*(2*ob._omega[0] + ob._omega[1]*np.cos(ob._theta[0] - ob._theta[1]))
    # p2 = ob._M[1]*ob._L[1]**2*(ob._omega[1] + ob._omega[0]*np.cos(ob._theta[0] - ob._theta[1]))
    # p = p1 + p2

    # P1.append(p1)
    # P2.append(p2)
    # P.append(p)
    
    # if ob._t % 1/1000 == 0:
    #     plt.cla()
    #     # ax2.cla()
    #     plt.plot(ob.x()[0],ob.y()[0], 'bo')
    #     plt.plot([0,ob.x()[0]], [0,ob.y()[0]], '-b')
    #     plt.plot(x2,y2,'ro')
    #     plt.plot([ob.x()[0],x2],[ob.y()[0],y2], '-r')
    #     plt.xlim([(-L)-L/5, (L)+L/5])  
    #     plt.ylim([(-L)-L/5, (L)+L/5])
    #     plt.xlabel('x [m]')
    #     plt.ylabel('y [m]')
    #     plt.title("t={:0.1f}".format(ob._t))
    #     # ax2.plot(0, KE, 'ro')
    #     # ax2.plot(0, PE, 'bo')
    #     # ax2.plot(0, E , 'go')
    #     # ax2.set_xlim(-1,1)
    #     # ax2.set_ylim(-10,250)
    #     plt.pause(0.0001)
    # print(ob._t)

plt.plot(ke, label = 'KE')
plt.plot(pe, label = 'PE')
plt.plot(e , label = 'E')
# plt.plot(P1, label = 'P1')
# plt.plot(P2, label = 'P2')
# plt.plot(P, label = 'P')
plt.legend()
plt.show()

# #Damping parameter 
# R = 1.0

# #driving amplitude
# A = 1.0

#check period with t= sqrt(l2 pi/g)