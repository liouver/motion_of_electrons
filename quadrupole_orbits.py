import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
sin = np.sin
cos = np.cos
sinh = np.sinh
cosh = np.cosh
sqrt = np.sqrt
V0 = 6.5 * 10**3  # V
a = 0.02  # m
L = 0.05  # m
c = 2.99792458 * 10**8  # m/s
m_e = 0.510999 * 10**6  # m/e, MV/c**2
Ek = 300  # keV
gamma = Ek / 510.999 + 1
beta = np.sqrt(1 - 1 / gamma**2)
E0 = 2 * V0 / a
k = E0 / (gamma * m_e * a * beta**2)
print(E0, sqrt(k) * L)
M_F = np.mat([[cos(sqrt(k) * L), 1 / sqrt(k) * sin(sqrt(k) * L)],
              [- sqrt(k) * sin(sqrt(k) * L), cos(sqrt(k) * L)]])
M_D = np.mat([[cosh(sqrt(k) * L), 1 / sqrt(k) * sinh(sqrt(k) * L)],
              [sqrt(k) * sinh(sqrt(k) * L), cosh(sqrt(k) * L)]])
M_L = np.mat([[1, L], [0, 1]])

X0 = np.mat([[1.5], [0.52]])
Y0 = np.mat([[1.5], [0.52]])
X = X0
Y = Y0
x = []
dx = []
y = []
dy = []
x.append(X[0, 0])
dx.append(X[1, 0])
y.append(Y[0, 0])
dy.append(Y[1, 0])
for i in range(10):
    X = M_F * X
    Y = M_D * X
    x.append(X[0, 0])
    dx.append(X[1, 0])
    y.append(Y[0, 0])
    dy.append(Y[1, 0])
    X = M_D * X
    Y = M_F * Y
    x.append(X[0, 0])
    dx.append(X[1, 0])
    y.append(Y[0, 0])
    dy.append(Y[1, 0])
z = np.arange(0, 105, 5)
fig, ax1 = plt.subplots()
ax1.plot(z, x, 'b', linewidth=2.5)
ax1.xaxis.grid()
ax1.set_xlabel('longitudinal position, z (cm)', fontsize=14)
ax1.set_ylabel('orbits, x (cm)', color='b', fontsize=14)
ax1.tick_params('y', colors='b')
ax1.tick_params('both', direction='in', labelsize=12)
ax1.set_xlim([0, 100])
ax1.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

ax2 = ax1.twinx()
ax2.plot(z, dx, 'r--', linewidth=2.5)
# ax2.yaxis.grid()
ax2.set_ylabel("x' (cm/s)", color='r', fontsize=14)
ax2.tick_params('y', colors='r', direction='in', labelsize=12)
plt.title("electron orbits in the FD quadrupole array")
fig.tight_layout()

plt.show()
