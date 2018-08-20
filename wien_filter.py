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
B_l = (pi / 2) * m_e * beta * gamma**2 / (c * (1 + G))  # T-m
E_l = beta * c * B_l  # V
E_R = m_e * (gamma**2 - 1) / gamma  # V

fig1, ax1 = plt.subplots()
ax1.plot(Ek, 10**4 * B_l, 'b', linewidth=2.5)
ax1.set_xlim([190, 410])
ax1.set_ylim([34.5, 73])
ax1.set_yticks([38, 45, 52, 59, 66, 73])
ax1.grid()
# ax1.xaxis.grid()
ax1.set_xlabel('Electron kinetic energy (keV)', fontsize=14)
ax1.set_ylabel('$B\cdot L$ ($Gauss\cdot m$)', color='b', fontsize=14)
ax1.tick_params('y', colors='b')
ax1.tick_params('both', direction='in', labelsize=12)

ax2 = ax1.twinx()
ax2.plot(Ek, E_l / 10**6, 'r', linewidth=2.5)
ax2.set_ylim([0.7, 1.8])
ax2.yaxis.grid()
ax2.set_ylabel('$E\cdot L$ (MV)', color='r', fontsize=14)
ax2.tick_params('y', colors='r', direction='in', labelsize=12)
# plt.title('magnetic and electric field for wien filter')
fig1.tight_layout()
plt.savefig('wienfilter_EB.pdf', format='pdf')
plt.show()
