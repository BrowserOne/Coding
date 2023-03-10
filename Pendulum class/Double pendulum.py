from methods import pendulum as pd
import matplotlib.pyplot as plt
import numpy as np

ob1 = pd(1, 10.0,theta_initial=90, setstep = 'Euler cromer')
ob2 = pd(0.5, 5.0,theta_initial=10, setstep = 'Euler cromer')
t_max = 100   #[s]
dt = 1/100    #[s]
L = ob1._L + ob2._L

#set up loop
while ob1._t<t_max:
    a1 = ((-ob1._g*(ob1._M+ob2._M)*np.sin(ob1._theta) - ob2._M*ob1._g*np.sin(ob1._theta - 2*ob2._theta) -
                                 2*np.sin(ob1._theta - ob2._theta)*ob2._M*((ob2._omega**2)*ob2._L + (ob1._omega**2)*ob1._L*np.cos(ob1._theta - ob2._theta)))/
                                 (ob1._L*(2*ob1._M + ob2._M - ob2._M*np.cos(2*ob1._theta - 2*ob2._theta))))
    a2 = ((2*np.sin(ob1._theta - ob2._theta)*((ob1._omega**2)*ob1._L*(ob1._M + ob2._M)+ ob1._g*(ob1._M + ob2._M)*np.cos(ob1._theta) + 
                                                                    (ob2._omega**2)*ob2._L*ob2._M*np.cos(ob1._theta - ob2._theta)))/
                                                                    (ob2._L*(2*ob1._M + ob2._M - ob2._M*np.cos(2*ob1._theta - 2*ob2._theta))))
    
    #increment velcoity account for angle being 0.0
    ob1.step(a1, dt)
    ob2.step(a2, dt)
    x2 = ob1.x() + ob2.x()
    y2 = ob1.y() + ob2.y()


    plt.cla()
    plt.plot(ob1.x(),ob1.y(), 'bo')
    plt.plot([0,ob1.x()], [0,ob1.y()], '-b')
    plt.plot(x2,y2,'ro')
    plt.plot([ob1.x(),x2],[ob1.y(),y2], '-r')
    plt.xlim([(-L)-L/5, (L)+L/5])  
    plt.ylim([(-L)-L/5, (L)+L/5])
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.title("t={:0.1f}".format(ob1._t))
    plt.pause(0.0001)



plt.show()

# #Damping parameter 
# R = 1.0

# #spring constant
# K = 1.0

# #driving amplitude
# A = 1.0

#check period with t= sqrt(l2 pi/g)