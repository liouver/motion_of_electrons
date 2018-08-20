import numpy as np
import matplotlib.pyplot as plt
import random

pi = np.pi
sin = np.sin
cos = np.cos
sinh = np.sinh
cosh = np.cosh
sqrt = np.sqrt
V0 = 10 * 10**3  # V
a1 = 0.06  # m
a2 = 0.06  # m
L = 0.1  # m quadrupole length
L1 = 0.005  # m drift length
c = 2.99792458 * 10**8  # m/s
m_e = 0.510999 * 10**6  # m/e, eV/c**2
Ek = 300  # kV
gamma = Ek / 510.999 + 1
beta = np.sqrt(1 - 1 / gamma**2)
# E0 = 2 * V0 / a
E01 = 0.1 * 10**6  # V/m
E02 = 0.1 * 10**6  # V/m
k1 = E01 / (gamma * m_e * a1 * beta**2)
k2 = E02 / (gamma * m_e * a2 * beta**2)
# print(sqrt(k1) * L)
M_F = np.mat([[cos(sqrt(k1) * L), 1 / sqrt(k1) * sin(sqrt(k1) * L)],
              [- sqrt(k1) * sin(sqrt(k1) * L), cos(sqrt(k1) * L)]])
M_D = np.mat([[cosh(sqrt(k2) * L), 1 / sqrt(k2) * sinh(sqrt(k2) * L)],
              [sqrt(k2) * sinh(sqrt(k2) * L), cosh(sqrt(k2) * L)]])
M_L = np.mat([[1, L1], [0, 1]])

epsilon = 4  # mm*mrad
alpha0 = 0  # no unit
beta0 = 400  # mm/mrad
gamma0 = 1 / 400  # mrad/mm
sigma = epsilon * np.mat([[beta0, alpha0], [alpha0, gamma0]])
c11 = []
c22 = []
c12 = []
z = []
c11.append(sigma[0, 0] / epsilon)
c22.append(sigma[1, 1] / epsilon)
c12.append(-sigma[0, 1] / epsilon)
z.append(0)
period_num = 10
types = 2
if types == 1:
    for i in range(period_num):
        sigma = M_F * sigma * M_F.getT()
        c11.append(sigma[0, 0] / epsilon)
        c22.append(sigma[1, 1] / epsilon)
        c12.append(-sigma[0, 1] / epsilon)
        z.append(z[-1] + L * 100)
        sigma = M_L * sigma * M_L.getT()
        c11.append(sigma[0, 0] / epsilon)
        c22.append(sigma[1, 1] / epsilon)
        c12.append(-sigma[0, 1] / epsilon)
        z.append(z[-1] + L1 * 100)
        sigma = M_D * sigma * M_D.getT()
        c11.append(sigma[0, 0] / epsilon)
        c22.append(sigma[1, 1] / epsilon)
        c12.append(-sigma[0, 1] / epsilon)
        z.append(z[-1] + L * 100)
        sigma = M_L * sigma * M_L.getT()
        c11.append(sigma[0, 0] / epsilon)
        c22.append(sigma[1, 1] / epsilon)
        c12.append(-sigma[0, 1] / epsilon)
        z.append(z[-1] + L1 * 100)
    x_max = np.sqrt(epsilon * np.array(c11))
elif types == 2:
    for i in range(period_num):
        sigma = M_F * sigma * M_F.getT()
        c11.append(sigma[0, 0] / epsilon)
        c22.append(sigma[1, 1] / epsilon)
        c12.append(-sigma[0, 1] / epsilon)
        z.append(z[-1] + L * 100)
        sigma = M_D * sigma * M_D.getT()
        c11.append(sigma[0, 0] / epsilon)
        c22.append(sigma[1, 1] / epsilon)
        c12.append(-sigma[0, 1] / epsilon)
        z.append(z[-1] + L * 100)
    x_max = np.sqrt(epsilon * np.array(c11))

wx = []
vxp = []
j = 0
xlim = 40
ylim = 1
while i < 10000:
    x = random.uniform(-1 * xlim, xlim)
    xp = random.uniform(-1 * ylim, ylim)
    if c22[j] * x**2 + 2 * c12[j] * x * xp + c11[j] * xp**2 <= epsilon:
        wx.append(x)
        vxp.append(xp)
    i += 1

fig1, ax1 = plt.subplots()
ax1.plot(z, x_max, 'b', linewidth=2.5)
ax1.xaxis.grid()
ax1.set_xlabel(r'longitudinal position, z (cm)', fontsize=14)
ax1.set_ylabel(r'$\sqrt{\epsilon_x\beta_x}, (mm)$', color='b', fontsize=14)
ax1.tick_params('y', colors='b')
ax1.tick_params('both', direction='in', labelsize=12)
# ax1.set_xlim([0, 10])
# ax1.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# plt.show()

fig2, ax2 = plt.subplots()
ax2.plot(wx, vxp, 'b.')
ax2.set_xlabel(r'x (mm)', fontsize=14)
ax2.set_ylabel(r"x' (mrad)", fontsize=14)
ax2.set_xlim([-1 * xlim, xlim])
ax2.set_ylim([-1 * ylim, ylim])
plt.show()