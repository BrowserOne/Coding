import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def double_pendulum(t, y, L1, L2, m1, m2):
    """
    Defines the system of differential equations for a double pendulum.

    Args:
    - t: float, current time
    - y: list of floats, current values of theta1, omega1, theta2, omega2
    - L1: float, length of the first pendulum
    - L2: float, length of the second pendulum
    - m1: float, mass of the first pendulum
    - m2: float, mass of the second pendulum

    Returns:
    - dydt: list of floats, derivatives of theta1, omega1, theta2, omega2
    """
    theta1, omega1, theta2, omega2 = y
    
    # Calculate the sin and cos of the angles
    sin1, cos1 = np.sin(theta1), np.cos(theta1)
    sin2, cos2 = np.sin(theta2), np.cos(theta2)
    
    # Define the constants and intermediate values
    g = 9.81
    a = (m1 + m2) * L1
    b = m2 * L2 * np.cos(theta1 - theta2)
    c = m2 * L1 * np.cos(theta1 - theta2)
    d = m2 * L2
    e = -m2 * L2 * omega2**2 * np.sin(theta1 - theta2) - (m1 + m2) * g * np.sin(theta1)
    f = m2 * L1 * omega1**2 * np.sin(theta1 - theta2) - m2 * g * np.sin(theta2)
    
    # Calculate the derivatives
    dydt = [omega1,
            (e*d - f*b) / (a*d - b*c),
            omega2,
            (a*f - c*e) / (a*d - b*c)]
    
    return dydt

# Define the parameters of the double pendulum
L1 = 1
L2 = 1
m1 = 1
m2 = 1
y0 = [np.pi/2, 0, np.pi/2, 0] # initial conditions

# Define the time range and solve the system of differential equations
t_span = [0, 10]
sol = solve_ivp(double_pendulum, t_span, y0, args=(L1, L2, m1, m2))

# Plot the results
plt.plot(sol.t, sol.y[0], label='theta1')
plt.plot(sol.t, sol.y[2], label='theta2')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Angle (rad)')
plt.pause(0.01)
plt.show()