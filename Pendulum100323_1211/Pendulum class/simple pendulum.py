from Setup import pendulum as pd
import matplotlib.pyplot as plt
import numpy as np

ob = pd(0.1, 10.0,theta = 90, setstep = 'Runge-kuttaSimple')
t_max = 100    #[s]
dt = 0.00025    #[s]
ke = []
pe = []
e = []

# fig, (ax1, ax2) = plt.subplots(1, 2)
#set up loop
while ob._t<t_max:
    # a = -(ob._g/ob._L)*np.sin(ob._theta)
    #increment velcoity account for angle being 0.0
    ob.step(dt)

    KE = (1/2)*ob._M*(ob._L*ob._omega)**2
    PE = ob._M*ob._g*(ob.y()+ob._L)
    E = KE + PE
    ke.append(KE)
    pe.append(PE)
    e .append( E)
    # ax1.cla()
    # ax2.cla()
    # ax1.plot(ob.x(),ob.y(), 'ro')
    # ax1.plot([0,ob.x()], [0,ob.y()], '-r')
    # ax1.set_xlim([(-ob._L)-ob._L/5, (ob._L)+ob._L/5])  
    # ax1.set_ylim([(-ob._L)-ob._L/5,(ob._L)+ob._L/5])
    # ax1.set_xlabel('x [m]')
    # ax1.set_ylabel('y [m]')
    # plt.title("t={:0.1f}".format(ob._t))
    # ax2.plot(0, KE, 'ro')
    # ax2.plot(0, PE, 'bo')
    # ax2.plot(0, E , 'go')
    # ax2.set_xlim(-1,1)
    # ax2.set_ylim(-10,50)
    # plt.pause(0.01)
plt.plot(ke, label = 'KE')
plt.plot(pe, label = 'PE')
plt.plot(e , label = 'E')
plt.legend()
plt.show()

# #Damping parameter 
# R = 1.0

# #spring constant
# K = 1.0

# #driving amplitude
# A = 1.0

#check period with t= sqrt(l2 pi/g)