import numpy as np
import matplotlib.pyplot as plt

ec = 1.60219e-19  # C
h_ = 1.05459e-34  # J*s, Planc constant
m_e = 9.109e-31  # kg, electron mass
c = 2.99792458 * 10**8  # m/s

L = 0.2  # m
# Ek = np.arange(0.1, 1e3)  # keV
Ek = 100
gamma = Ek / 510.999 + 1
beta = np.sqrt(1 - 1 / gamma**2)
B_z = 0.01  # T/m
mu_z = ec * h_ / m_e / 2  # J/T, N*m/T
F_z = mu_z * B_z  # N
t = L / (beta * c)  # s
S = 0.5 * F_z / (gamma * m_e) * t**2  # m
t1 = 10 * t
S1 = S + F_z / (gamma * m_e) * t * t1

R = 0.01  # m
# R = np.arange(1e-4, 1e-1, 1e-3)
B0 = B_z * R  # T
E0 = B0 * beta * c  # V/m
V = E0 * R / 2  # V

AA = np.pi * gamma * beta * m_e * c / ec / B0

print(S, S1, B0, E0/R, V, AA)


def plot_distance():
    fig, ax = plt.subplots()
    ax.loglog(Ek, S)
    ax.set_xlabel(r'Electron energy (eV)', fontsize=16)
    ax.set_ylabel(r'Distance (m)', fontsize=16)
    ax.set_xlim([0.1, 1e3])
    ax.set_ylim([1e-9, 1e-5])
    ax.tick_params(which='both', direction='in', labelsize=14)
    # ax.legend([r'deflection distance'], frameon=False, fontsize=14, loc=4)
    plt.tight_layout()
    plt.savefig('deflection_distance.pdf', format='pdf')
    plt.show()


def plot_voltage():
    fig, ax1 = plt.subplots()
    ax1.loglog(Ek, V)
    ax1.set_xlabel(r'Electron energy (eV)', fontsize=16)
    ax1.set_ylabel(r'Voltage (V)', fontsize=16)
    # ax1.set_xlim([0.1, 1e3])
    # ax1.set_ylim([1e2, 1e4])
    ax1.tick_params(which='both', direction='in', labelsize=14)
    ax1.legend([r'R=0.005 m'], frameon=False, fontsize=14, loc=4)
    plt.tight_layout()
    plt.savefig('quadrupole_voltage_E.pdf', format='pdf')
    plt.show()


def plot_voltage_R():
    fig, ax1 = plt.subplots()
    ax1.loglog(R, V)
    ax1.set_xlabel(r'Radius (m)', fontsize=16)
    ax1.set_ylabel(r'Voltage (V)', fontsize=16)
    # ax1.set_xlim([0.1, 1e3])
    # ax1.set_ylim([1e2, 1e4])
    ax1.tick_params(which='both', direction='in', labelsize=14)
    # ax1.legend([r'deflection distance'], frameon=False, fontsize=14, loc=4)
    plt.tight_layout()
    plt.savefig('quadrupole_voltage_R.pdf', format='pdf')
    plt.show()


# plot_distance()
