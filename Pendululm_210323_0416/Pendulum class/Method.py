"""

"""


import numpy as np

class method:
    def __init__(self, L, M, theta_now, omega_now, t, g):
        self._L = L
        self._M = M
        self._t = t
        self._g = g
        self._omega = omega_now
        self._theta = theta_now

    def a_simple(self, theta):
        a = (self._g/self._L)*np.sin(theta)
        return a
    
    def a_double(self, theta, omega):
        a1 = ((-(self._M[0]+self._M[1])*self._g*self._L[0]*np.sin(theta[0]) - self._M[1]*self._L[0]*self._L[1]*(omega[1])**2*np.sin(theta[0] - theta[1]) +
               self._M[1]*self._g*self._L[0]*np.sin(theta[1])*np.cos(theta[0] - theta[1]) - 
               self._M[1]*(self._L[0])**2*(omega[0])**2*np.sin(theta[0]- theta[1])*np.cos(theta[0] - theta[1]))/
               ((self._M[0] + self._M[1])*(self._L[0])**2 - self._M[1]*(self._L[0])**2*(np.cos(theta[0] - theta[1]))**2))
        a2 = ((self._M[1]*np.cos(theta[0] - theta[1])*(-(self._M[0] + self._M[1])*self._g*self._L[0]*np.sin(theta[0]) - 
                                                                  self._M[1]*self._L[0]*self._L[1]*(omega[1])**2*np.sin(theta[0] - theta[1])) + 
              (self._M[0] + self._M[1])*self._M[1]*self._L[0]*self._g*np.sin(theta[1]) - 
              (self._M[0] + self._M[1])*self._M[1]*(self._L[0])**2*(omega[0])**2*np.sin(theta[0] - theta[1]))/
              (-(self._M[0] + self._M[1])*self._L[0]*self._L[1]*self._M[0] + (self._M[1])**2*self._L[0]*self._L[1]*(np.cos(theta[0] - theta[1]))**2))
        return np.array([a1,a2])

    def euler_simple(self,dt):
        omega_next = self._omega + self.a_simple(self._theta)*dt
        self._theta = self._theta + self._omega*dt
        return self._theta, omega_next
    
    def euler_double(self,dt):
        omega_next = self._omega + self.a_double(self._theta, self._omega)*dt
        self._theta = self._theta + self._omega*dt
        return self._theta, omega_next
    
    def euler_cromer_simple(self, dt):
        self._omega = self._omega + self.a_simple(self._theta)*dt
        self._theta = self._theta + self._omega*dt
        return self._theta, self._omega
    
    def euler_cromer_double(self, dt):
        self._omega = self._omega + self.a_double()*dt
        self._theta = self._theta + self._omega*dt
        return self._theta, self._omega

    def runge_kutta_simpleO2(self, dt):
            u1 = self.a_simple(self._theta)
            k1 = self._omega
            u2 = self.a_simple(self._theta + k1*dt*(2/3))
            k2 = self._omega + u2*dt*(2/3)
            omega_next = self._omega + ((1/4)*u1 + (2/3)*u2)*dt
            theta_next = self._theta + ((1/4)*k1 + (2/3)*k2)*dt
            return theta_next, omega_next
    
    def runge_kutta_simple(self, dt):
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
