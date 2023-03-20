import numpy as np
import matplotlib.pyplot as plt

#Set initial values

g = -9.81       #[m/s^2]
l1 = 1        #[m]
l2 = 0.5      #[m]
m1 = 10         #[Kg]
m2 = 5          #[Kg]

#time step
dt = 1/500  #[s]
t = 0.0         #[s]
t_max= 100       #[s]


#define positions of 1 and reletive position 1,2
theta1_now = np.radians(10)
theta2_now = np.radians(10)
x1_now = l1*np.sin(theta1_now)
x12_now = l2*np.sin(theta2_now)     #relative x position of 2
y1_now = l1*np.cos(theta1_now)
y12_now = l2*np.cos(theta2_now)

#define next step for pendulum
y1_next = y1_now
y12_next = y12_now
theta1_next = theta1_now
theta2_next = theta2_now
x1_next = x1_now
x12_next = x12_now

#define omega
omega1_now = 0.0
omega2_now = 0.0

#set postion of 2
y2_now = y1_now + y12_now
x2_now = x1_now + x12_now

#account for possible range of graph
L = l1 + l2

#plot inital values
plt.plot(x1_now,y1_now, 'bo')
plt.plot([0,x1_now], [0,y1_now], '-b')
plt.plot(x2_now,y2_now,'ro')
plt.plot([x1_now,x2_now],[y1_now,y2_now], '-r')
plt.xlim([(-L)-L/5, (L)+L/5])  
plt.ylim([(-L)-L/5, (L)+L/5])
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title("t={:0.1f}".format(t))

while t<t_max:
    #increment theta and omega
    omega1_next = omega1_now + ((-g*(2*m1+m2)*np.sin(theta1_now) - m2*g*np.sin(theta1_now - 2*theta2_now) -
                                 2*np.sin(theta1_now - theta2_now)*m2*((omega2_now**2)*l2 + (omega1_now**2)*l1*np.cos(theta1_now - theta2_now)))/
                                 (l1*(2*m1 + m2 - m2*np.cos(2*theta1_now - 2*theta2_now))))*dt
    omega2_next = omega2_now + ((2*np.sin(theta1_now - theta2_now)*((omega1_now**2)*l1*(m1 + m2)+ g*(m1 + m2)*np.cos(theta1_now) + 
                                                                    (omega2_now**2)*l2*m2*np.cos(theta1_now - theta2_now)))/
                                                                    (l2*(2*m1 + m2 - m2*np.cos(2*theta1_now - 2*theta2_now))))*dt
    theta1_next = theta1_now + omega1_next*dt
    theta2_next = theta2_now + omega2_next*dt

    #shuffle values
    theta1_now = theta1_next
    theta2_now = theta2_next
    omega1_now = omega1_next
    omega2_now = omega2_next
    t = t+dt

    #set x y position based on theta
    x1_now = l1*np.sin(theta1_now)
    y1_now = l1*np.cos(theta1_now)
    x12_now = l2*np.sin(theta2_now)
    y12_now = l2*np.cos(theta2_now)
    y2_now = y1_now + y12_now
    x2_now = x1_now + x12_now


    plt.cla()
    plt.plot(x1_now,y1_now, 'bo')
    plt.plot([0,x1_now], [0,y1_now], '-b')
    plt.plot(x2_now,y2_now,'ro')
    plt.plot([x1_now,x2_now],[y1_now,y2_now], '-r')
    plt.xlim([(-L)-L/5, (L)+L/5])  
    plt.ylim([(-L)-L/5, (L)+L/5])
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.title("t={:0.1f}".format(t))
    plt.pause(0.01)

plt.show()
