from methods import pendulum as pd
import matplotlib.pyplot as plt
import numpy as np

ob = pd(0.1, 10.0)
t_max = 6    #[s]
dt = 1/500      #[s]


#set up loop
while ob._t<t_max:
    a = -(ob._g/ob._L)*np.sin(ob._theta)
    #increment velcoity account for angle being 0.0
    ob.step(a, dt)

    plt.cla()
    plt.plot(ob.x(),ob.y(), 'ro')
    plt.plot([0,ob.x()], [0,ob.y()], '-r')
    plt.xlim([(-ob._L)-ob._L/5, (ob._L)+ob._L/5])  
    plt.ylim([(-ob._L)-ob._L/5,(ob._L)+ob._L/5])
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.title("t={:0.1f}".format(ob._t))
    plt.pause(0.01)



plt.show()

# #Damping parameter 
# R = 1.0

# #spring constant
# K = 1.0

# #driving amplitude
# A = 1.0

#check period with t= sqrt(l2 pi/g)