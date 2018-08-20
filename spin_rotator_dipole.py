import numpy as np
import matplotlib.pyplot as plt

c = 2.99792458 * 10**8
m_e = 0.510999 * 10**6  # m/e, MV/c**2
# dEk = 100
# N = 2 * dEk / 0.1 + 1
Ek = np.linspace(10, 10000, 4901)
gamma = Ek / 510.999 + 1
beta = np.sqrt(1 - 1 / gamma**2)
G = 0.00115965
Phi = 90  # degree, beam bent degree
#################################################

phi_B = Phi * G * gamma
phi_E = Phi * (G * gamma**2 - G - 1) / gamma

fig1, ax1 = plt.subplots()
ax1.semilogx(Ek, phi_E, 'b', linewidth=2.5)
ax1.set_xlim([10, 10000])
ax1.set_ylim([-90, 0])
ax1.grid(True, which='both')
ax1.set_xlabel('Electron kinetic energy (keV)', fontsize=14)
ax1.set_ylabel('Spin rotation degree for E-dipole ($^\circ$)',
               color='b', fontsize=14)
ax1.tick_params('y', colors='b')
ax1.tick_params(which='both', direction='in', labelsize=12)

ax2 = ax1.twinx()
ax2.semilogx(Ek, phi_B, 'r', linewidth=2.5)
# ax2.set_ylim([0.143, 0.188])
# ax2.set_yticks([0.146, 0.152, 0.158, 0.164, 0.17, 0.176, 0.182, 0.188])
ax2.yaxis.grid()
ax2.set_ylabel('Spin rotation degree for B-dipole ($^\circ$)',
               color='r', fontsize=14)
ax2.tick_params('y', colors='r', direction='in', labelsize=12)
plt.title('Spin rotation degree for beam bending 90$^\circ$', fontsize=16)

fig1.tight_layout()
plt.show()
plt.savefig('spin_rotation.pdf', format='pdf')
