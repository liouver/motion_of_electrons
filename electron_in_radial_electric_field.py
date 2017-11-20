# solve the motion of electrons with low energy (gamma = 1) in radial E
# (cylindrical coordinates)
from scipy.integrate import odeint
import numpy as np
from sympy import *
try:
    import matplotlib.pyplot as plt
except ImportError:
    import matplotlib.pylab as plt

c = 2.99792458 * 10**8  # m/s
m = 0.5109989461 * 10**6  # eV/c**2
e_m = c**2 / m  # e/m = m*m/s*s*V

Ek_0 = 0.3  # MeV
gamma_0 = Ek_0 / 0.5109989461 + 1
R2 = 0.14  # m
R1 = 0.1  # m


def motion_equation(s, x, E_r):
    r, dr, theta, dtheta = s.tolist()
    d2r = symbols('d2r')
    d2theta = symbols('d2theta')
    gamma = (1 - (dr**2 + r**2 * dtheta**2) / c**2)**(-1 / 2)
    dgamma = gamma**3 * (dr * d2r + r * dr * dtheta**2 +
                         r**2 * dtheta * d2theta) / c**2
    eq1 = dgamma * dr + gamma * d2r - gamma * r * dtheta**2 + e_m * E_r / r
    eq2 = dgamma * r * dtheta + 2 * gamma * dr * dtheta + gamma * r * d2theta
    result_sol = solve([eq1, eq2], [d2r, d2theta])
    [d2r, d2theta] = result_sol.values()
    if R1 < r < R2:
        return [dr, d2r, dtheta, d2theta]
    else:
        raise ValueError('Out of the range, electron reaches to the plate')


def main():
    vel = c * np.sqrt(1 - 1 / gamma_0**2)  # velocity, m/s
    r_0 = 0.12  # m
    dr_0 = 0  # m/s
    theta_0 = 0  # rad
    dtheta_0 = 1.0 * vel / r_0  # rad/s
    E_r = c**2 * (gamma_0**2 - 1) / (e_m * gamma_0)
    t = np.linspace(0, 1.0 * 10**(-9), 21)
    s_init = [r_0, dr_0, theta_0, dtheta_0]
    args = (E_r,)
    s_sol = odeint(motion_equation, s_init, t, args)

    plt.figure()
    plt.plot((s_sol[:, 0] * np.cos(s_sol[:, 2])),
             (s_sol[:, 0] * np.sin(s_sol[:, 2])))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


if __name__ == '__main__':
    main()
