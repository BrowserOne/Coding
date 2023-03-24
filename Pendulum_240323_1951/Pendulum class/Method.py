"""
Program to calculate next step in pendulum motion. Script is divided into simple pendulum and double pendulum calculation.

Author: Sreecharan Chakrala
Date:21/03/2023
Email:S.chakrala@lancaster.ac.uk
"""
#import required modules
import numpy as np

class method:
    def __init__(self, L, M, theta_now, omega_now, t, g):
        """
                Define variables of pendulum object

        Arguments:
        ----------
            L: Length of pendulum               [m]
            M: Mass of pendulum                 [kg]
            t: Current time in iteration        [s]
            g: Gravitational constant
            omega: Angular velocity of pendulum
            theta: Angular position of pendulum
        """
        self._L = L         #[m]
        self._M = M         #[Kg]
        self._t = t         #[s]
        self._g = g
        self._omega = omega_now
        self._theta = theta_now

    def a_simple(self, theta):
        """
        Define physics of a simple pendulum system used to iterate angular velocity of a simple pendulum by one step based on the angular position.

        Arguments:
        ----------
            self._g: Gravitational acceleration of pendulum system
            self._L: Length of the pendulum object

        Returns:
        --------
            a: Change in angular velocity based on angular position.
        """
        a = -(self._g/self._L)*np.sin(theta)
        return a
    
    def a_double(self, theta, omega):
        """
        Define physics of a double pendulum system used to iterate angular velocity of the pendulum system by one step based on the angular position.

        Arguments:
        ----------
            self._g: Gravitational acceleration of pendulum system
            self._L: List containing length of both pendulum objects
            self._M: List containing mass of both pendulum objects
            theta: Angular position of the pendulum inputted separately from current position as some iteration methods call function more then once per iteration
            omega: Angular velocity of the pendulum inputted separately from current velocity as some iteration methods call function more than once per iteration

        Returns:
        --------
            a1: Change in angular velocity of the first pendulum (connected to the origin) based on angular position and velocity
            a2: Change in angular velocity of the second pendulum (connected to the first pendulum) based on angular position and velocity
        """
        #Define step in velocity of first pendulum based on previous step in velocity and position of all pendulums in the system
        a1 = ((-(self._M[0]+self._M[1])*self._g*self._L[0]*np.sin(theta[0]) - self._M[1]*self._L[0]*self._L[1]*(omega[1])**2*np.sin(theta[0] - theta[1]) +
               self._M[1]*self._g*self._L[0]*np.sin(theta[1])*np.cos(theta[0] - theta[1]) - 
               self._M[1]*(self._L[0])**2*(omega[0])**2*np.sin(theta[0]- theta[1])*np.cos(theta[0] - theta[1]))/
               ((self._M[0] + self._M[1])*(self._L[0])**2 - self._M[1]*(self._L[0])**2*(np.cos(theta[0] - theta[1]))**2))
        #Define step in velocity of second pendulum based on previous step in velocity and position of all pendulums in the system
        a2 = ((np.cos(theta[0] - theta[1])*(-(self._M[0] + self._M[1])*self._g*self._L[0]*np.sin(theta[0]) - 
                                                                  self._M[1]*self._L[0]*self._L[1]*(omega[1])**2*np.sin(theta[0] - theta[1])) + 
              (self._M[0] + self._M[1])*self._L[0]*self._g*np.sin(theta[1]) - (self._M[0] + self._M[1])*(self._L[0])**2*(omega[0])**2*np.sin(theta[0] - theta[1]))/
              (-(self._M[0] + self._M[1])*self._L[0]*self._L[1] + self._M[1]*self._L[0]*self._L[1]*(np.cos(theta[0] - theta[1]))**2))
        return np.array([a1,a2])

    def euler_simple(self,dt):
        """
        Function iterating motion of a simple pendulum based on the forward euler method.

        Arguments:
        ----------
            self:       Object containing attributes of the pendulum
            dt:         Time step for the motion of pendulums
            a_simple(): Function defining physics of a simple pendulum and change in angular velocity based on position

        Returns:
        --------
            self._theta: Next step in angular position 
            self._omega: Next step in angular velocity
        """
        omega_next = self._omega + self.a_simple(self._theta)*dt
        self._theta = self._theta + self._omega*dt
        return self._theta, omega_next
    
    def euler_double(self,dt):
        """
        Function iterating motion of a double pendulum system based on the forward euler method.

        Arguments:
        ----------
            self:       Object containing attributes of the pendulum
            dt:         Time step for the motion of pendulums
            a_double(): Function defining physics of a double pendulum system and next step in angular velocity based on current angular velocity and position

        Returns:
        --------
            self._theta: List containing next step in angular position of pendulum system
            self._omega: List containing next step in angular velocity of pendulum system
        """
        omega_next = self._omega + self.a_double(self._theta, self._omega)*dt
        self._theta = self._theta + self._omega*dt
        return self._theta, omega_next
    
    def euler_cromer_simple(self, dt):
        """
        Function iterating motion of a simple pendulum based on the euler cromer method.

        Arguments:
        ----------
            self:       Object containing attributes of the pendulum
            dt:         Time step for the motion of pendulums
            a_simple(): Function defining physics of a simple pendulum and change in angular velocity based on position

        Returns:
        --------
            self._theta: Next step in angular position 
            self._omega: Next step in angular velocity
        """
        self._omega = self._omega + self.a_simple(self._theta)*dt
        self._theta = self._theta + self._omega*dt
        return self._theta, self._omega
    
    def euler_cromer_double(self, dt):
        """
        Function iterating motion of a double pendulum system based on the forward euler method.

        Arguments:
        ----------
            self:       Object containing attributes of the pendulum
            dt:         Time step for the motion of pendulums
            a_double(): Function defining physics of a double pendulum system and next step in angular velocity based on current angular velocity and position

        Returns:
        --------
            self._theta: List containing next step in angular position of pendulum system
            self._omega: List containing next step in angular velocity of pendulum system
        """
        self._omega = self._omega + self.a_double()*dt
        self._theta = self._theta + self._omega*dt
        return self._theta, self._omega

    def runge_kutta_simpleO2(self, dt):
        """
        Function iterating motion of a simple pendulum based on the second order Runge Kutta method. Method iterates motion of a pendulum by 2/3 of a time step and 
        summing a weighted sum of 2/3 step with 1/4 step.

        Arguments:
        ----------
            self:       Object containing attributes of the pendulum
            dt:         Time step for the motion of pendulums
            a_simple(): Function defining physics of a simple pendulum system and next step in angular velocity based on current angular position

        Returns:
        --------
            theta_next: Next step in angular position of pendulum system
            omega_next: Next step in angular velocity of pendulum system
        """
        u1 = self.a_simple(self._theta)
        k1 = self._omega
        u2 = self.a_simple(self._theta + k1*dt*(2/3))
        k2 = self._omega + u2*dt*(2/3)
        omega_next = self._omega + ((1/4)*u1 + (2/3)*u2)*dt
        theta_next = self._theta + ((1/4)*k1 + (2/3)*k2)*dt
        return theta_next, omega_next
    
    def runge_kutta_simple(self, dt):
        """
        Function iterating motion of a simple pendulum based on the forth order Runge Kutta method. Method iterates velocity of a pendulum by 1/2 of a time step
        based on a_simple function to define physics of system, calculating change full step in position based on 1/2 step of velocity. Repeats iteration 2 other
        times too calculate a more acuate full step calculation of angular position and velocity.

        Arguments:
        ----------
            self:       Object containing attributes of the pendulum
            dt:         Time step for the motion of pendulums
            a_simple(): Function defining physics of a simple pendulum system and next step in angular velocity based on current angular position

        Returns:
        --------
            theta_next: Next step in angular position of pendulum system
            omega_next: Next step in angular velocity of pendulum system
        """
        u1 = self.a_simple(self._theta)
        k1 = self._omega
        u2 = self.a_simple(self._theta + k1*dt*(1/2))
        k2 = self._omega + u2*dt*(1/2)
        u3 = self.a_simple(self._theta + k2*dt*(1/2))
        k3 = self._omega + u3*dt*(1/2)
        u4 = self.a_simple(self._theta + k3*dt*(1/2))
        k4 = self._omega + u4*dt
        omega_next = self._omega + (1/6)*(u1 + 2*u2 + 2*u3 + u4)*dt
        theta_next = self._theta + (1/6)*(k1 + 2*k2 + 2*k3 + k4)*dt
        return theta_next, omega_next
    
    def runge_kutta_double(self, dt):
        """
        Function iterating motion of a double pendulum system based on the forth order Runge Kutta method. Method iterates velocity of a pendulum by 1/2 of a time step
        based on a_double function to define physics of system, calculating change full step in position based on 1/2 step of velocity. Repeats iteration 2 other
        times too calculate a more acuate full step calculation of angular position and velocity.

        Arguments:
        ----------
            self:       Object containing attributes of the pendulum
            dt:         Time step for the motion of pendulums
            a_double(): Function defining physics of a double pendulum system and next step in angular velocity based on current angular position and velocity

        Returns:
        --------
            theta_next: Next step in angular position of pendulum system
            omega_next: Next step in angular velocity of pendulum system
        """
        u1 = self.a_double(self._theta, self._omega)
        k1 = self._omega
        u2 = self.a_double(self._theta + k1*dt*(1/2), k1)
        k2 = self._omega + u2*dt*(1/2)
        u3 = self.a_double(self._theta + k2*dt*(1/2), k2)
        k3 = self._omega + u3*dt*(1/2)
        u4 = self.a_double(self._theta + k3*dt*(1/2), k3)
        k4 = self._omega + u4*dt
        omega_next = self._omega + (1/6)*(u1 + 2*u2 + 2*u3 + u4)*dt
        theta_next = self._theta + (1/6)*(k1 + 2*k2 + 2*k3 + k4)*dt
        return theta_next, omega_next
    

# #Damping parameter 
# R = 1.0

# #driving amplitude
# A = 1.0

#check period with t= sqrt(l2 pi/g)

'compare method to scipy'
