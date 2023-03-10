import numpy as np

class pendulum:
    def __init__(self, L, M, t = 0.0, g = -9.81, theta_initial = 170, omega_initial = 0.0, setstep = 'Euler'):
        self._L = L
        self._M = M
        self._t = t
        self._g = g
        self._omega = omega_initial
        self._theta = np.radians(theta_initial)
        self._setstep = setstep

    def step(self, a , dt):
        if self._setstep == 'Euler':
            self._t += dt
            return self.Euler(a, dt)
        elif self._setstep == 'Euler cromer':
            self._t += dt
            return self.Euler_cromer(a,dt)

    def Euler(self, a, dt):
        omega_now = self._omega
        self._omega = self._omega + a*dt
        self._theta = self._theta + omega_now*dt
    
    def Euler_cromer(self, a, dt):
        self._omega = self._omega + a*dt
        self._theta = self._theta + self._omega*dt

    def Runge_Kutta(self, a, dt):
        t = self._t
    
    def x(self):
        return self._L*np.sin(self._theta)
    
    def y(self):
        return self._L*np.cos(self._theta)
