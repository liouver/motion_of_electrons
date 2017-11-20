# solve the motion of electrons with low energy (gamma = 1) in E & B
# (cartesiaan coordinates)

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D


def motion_equation(s, t):
    e_m = 9 * 10**10 / 0.51  # e/m = m*m/s*s*V
    (B_x, B_y, B_z) = (0, 0, 1 * 10**(-2))  # T
    (E_x, E_y, E_z) = (0, 1 * 10**2, 0)  # V/m
    dx = s[1]
    d2x = -e_m * (E_x + s[3] * B_z - s[5] * B_y)
    dy = s[3]
    d2y = -e_m * (E_y + s[5] * B_x - s[1] * B_z)
    dz = s[5]
    d2z = -e_m * (E_z + s[1] * B_y - s[3] * B_x)
    return [dx, d2x, dy, d2y, dz, d2z]


(x_0, xx_0, y_0, yy_0, z_0, zz_0) = (0, 2 * 10 ** 4, 1, 0 * 10 ** 4, 0, 0)
# m, m/s

t = np.linspace(0, 1 * 10**(-8), 1001)
s_init = [x_0, xx_0, y_0, yy_0, z_0, zz_0]
s_sol = odeint(motion_equation, s_init, t)

fig = plt.figure()
# ax = Axes3D(fig)
# ax.plot(s_sol[:, 0], s_sol[:, 2], s_sol[:, 4])
plt.plot(s_sol[:, 0], s_sol[:, 2])
plt.xlabel('x')
plt.ylabel('y')
plt.show()
