"""

"""

import numpy as np
from Method import method

class pendulum:
    def __init__(self, L, M, t = 0.0, g =  9.81, theta = 170, omega = 0.0, setstep = 'EulerSimple'):
        self._L = L
        self._M = M
        self._t = t
        self._g = g
        self._omega = omega
        self._theta = np.radians(theta)
        self._setstep = setstep

    def step(self, dt):
        md = method(self._L,self._M, self._theta, self._omega, self._t, self._g)
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

    
    def x(self):
        return self._L*np.sin(self._theta)
    
    def y(self):
        return  -self._L*np.cos(self._theta)
