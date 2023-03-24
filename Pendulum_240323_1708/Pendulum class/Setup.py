"""
Set class(pendulum) to create pendulum object and chose method use to iterate motion.

Author: Sreecharan Chakrala
Date:21/03/2023
Email:S.chakrala@lancaster.ac.uk
"""

#Import required modules
import numpy as np

#Import method class from Method file
from Method import method

#Start pendulum class
class pendulum:
    def __init__(self, L, M, t = 0.0, g =  9.81, theta = 170, omega = 0.0, setstep = 'EulerSimple'):
        """
        Define variables of pendulum object

        Arguments:
            L: Length of pendulum               [m]
            M: Mass of pendulum                 [kg]
            t: Current time in iteration        [s]
            t_max: Max runtime of simulation    [s]
            g: Gravitational constant
            omega: Angular velocity of pendulum
            theta: Angular position of pendulum

            setstep: Integration method used in calculation of motion.
                     Valid options include:
                        -EulerSimple:
                        ..
        """
        self._L = L                 #[m]
        self._M = M                 #[Kg]
        self._t = t                 #[s]
        self._g = g
        self._omega = omega

        #Convert angular position from pendulum from degrees to radians
        self._theta = np.radians(theta)
        self._setstep = setstep     #[s]

    def step(self, dt):
        """
        Function to call iteration method from method class

        Valid options:
        -------------
        ....

        Arguments:
        ----------
            self: object containing attributes of the pendulum
            dt: time step for the motion of pendulums

        Returns:
        --------
            theta: updated angular position of the pendulum
            omega: updated angular velocity of the pendulum
        """

        # Create object in method class to iterate motion of pendulum object
        md = method(self._L,self._M, self._theta, self._omega, self._t, self._g)

        #set statement to apply step function using selected iteration method
        if self._setstep == 'EulerSimple':
            self._t += dt
            self._theta, self._omega =  md.euler_simple(dt)
        elif self._setstep == 'EulerDouble':
            self._t += dt
            self._theta, self._omega = md.euler_double(dt)
        elif self._setstep == 'EulerCromerSimple':
            self._t += dt
            self._theta, self._omega = md.euler_cromer_simple(dt)
        elif self._setstep == 'EulerCromerDouble':
            self._t += dt
            self._theta, self._omega = md.euler_cromer_double(dt)      
        elif self._setstep == 'Runge-kuttaSimple':
            self._t += dt
            self._theta, self._omega = md.runge_kutta_simple(dt)
        elif self._setstep == 'Runge-KuttaDouble':
            self._t += dt
            self._theta, self._omega = md.runge_kutta_double(dt)
        else :
            raise ValueError("Invalided integration defined")

    def valid(self):
        """

        """

        # Create object in method class to iterate motion of pendulum object
        md = method(self._L,self._M, self._theta, self._omega, self._t, self._g)

        #set omega dot values so calculation is only run once
        a1 = md.a_double(self._theta, self._omega)[0]
        a2 = md.a_double(self._theta, self._omega)[1]

        #assign right hand side and left hand side of equations to check validity of equations
        rhs1 = ((self._M[0]+self._M[1])*self._L[0]**2*a1 + self._M[1]*self._L[0]*self._L[1]*a2*np.cos(self._theta[0] - self._theta[1]) +
                self._M[1]*self._L[0]*self._L[1]*self._omega[1]**2*np.sin(self._theta[0] - self._theta[1])) 
        lhs1 = (-(self._M[0]+self._M[1])*self._g*self._L[0]*np.sin(self._theta[0]))
        rhs2 = (self._M[1]*self._L[1]**2*a2 + self._M[1]*self._L[0]*self._L[1]*a1*np.cos(self._theta[0] - self._theta[1]) - 
                self._M[1]*self._L[0]*self._L[1]*self._omega[0]**2*np.sin(self._theta[0] - self._theta[1]))
        lhs2 = -self._M[1]*self._g*self._L[1]*np.sin(self._theta[1])

        #test validity of results
        if rhs1 == lhs1 and rhs2 == lhs2:
            return 0
        else :
            # print(rhs1, lhs1)
            return 1
 
    def x(self):
        """
        return x axis position of pendulum

        Arguments:
        ----------
            self._L: length of the pendulum
            self._theta: angular position of pendulum

        Returns:
        --------
            x position of pendulum
        """
        return self._L*np.sin(self._theta)
    
    def y(self):
        """
        return y axis position of pendulum

        Arguments:
        ----------
            self._L: length of the pendulum
            self._theta: angular position of pendulum

        Returns:
        --------
            y position of pendulum
        """
        return  -self._L*np.cos(self._theta)
