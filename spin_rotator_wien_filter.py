'''eletrical dipole spin rotator rotate spin direction 90 degree for E_k =300
    keV. the rotation of spin is not 90 degree when energy is not 300 keV. use
    wien filter to offset the spin rotation loss when energy is not 300 keV.
    This code calculate the spin rotation degree & E for spin rotator, and the
    E & B for wien filter at different energy
    Created by W. Liu @ Nov, 2017'''

import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
c = 2.99792458 * 10**8
m_e = 0.510999 * 10**6  # m/e, MV/c**2
dEk = 100
N = 2 * dEk / 0.1 + 1
Ek = np.linspace(300 - dEk, 300 + dEk, int(N))
gamma = Ek / 510.999 + 1
beta = np.sqrt(1 - 1 / gamma**2)
G = 0.00115965
Phi = pi * gamma[int(N / 2)] / (2 * (G * gamma[int(N / 2)]**2 - G - 1))
phi = Phi * (G * gamma**2 - G - 1) / gamma
B_l = (pi / 2 - phi) * m_e * beta * gamma**2 / (c * (1 + G))  # T-m
E_l = beta * c * B_l  # V
E_R = m_e * (gamma**2 - 1) / gamma  # V

fig1, ax1 = plt.subplots()
ax1.plot(Ek, 10**4 * B_l, 'b', linewidth=2.5)
ax1.set_xlim([190, 410])
ax1.set_ylim([-6, 8])
ax1.grid()
# ax1.xaxis.grid()
ax1.set_xlabel('Electron beam energy (keV)', fontsize=14)
ax1.set_ylabel(r'$B\cdot L$ ($Gauss\cdot m$)', color='b', fontsize=14)
ax1.tick_params('y', colors='b')
ax1.tick_params('both', direction='in', labelsize=12)

ax2 = ax1.twinx()
ax2.plot(Ek, E_l / 10**3, 'r', linewidth=2.5)
ax2.set_ylim([-150, 200])
ax2.yaxis.grid()
ax2.set_ylabel(r'$E\cdot L$ (kV)', color='r', fontsize=14)
ax2.tick_params('y', colors='r', direction='in', labelsize=12)
# plt.title('magnetic and electric field for wien filter')
fig1.tight_layout()
plt.savefig('wien_filter_offset_B_E.pdf', format='pdf')

fig2, ax3 = plt.subplots()
ax3.plot(Ek, phi * 180 / pi, 'b', linewidth=2.5)
ax3.set_xlim([190, 410])
ax3.set_ylim([78, 104])
ax3.set_yticks([78, 82, 86, 90, 94, 98, 102])
ax3.grid()
ax3.set_xlabel('Electron beam energy (keV)', fontsize=14)
ax3.set_ylabel(r'Spin degree ($^\circ$)', color='b', fontsize=14)
ax3.tick_params('y', colors='b')
ax3.tick_params('both', direction='in', labelsize=12)

ax4 = ax3.twinx()
ax4.plot(Ek, E_R / 10**3, 'r', linewidth=2.5)
ax4.set_ylim([330, 645])
ax4.set_yticks([320, 370, 420, 470, 520, 570, 620])
ax4.yaxis.grid()
ax4.set_ylabel(r'$E\cdot R$ (kV)', color='r', fontsize=14)
ax4.tick_params('y', colors='r', direction='in', labelsize=12)
# plt.title('spin rotation angle and electric field for dipole')
fig2.tight_layout()
plt.savefig('dipole_spin_angle_ER.pdf', format='pdf')

plt.show()
