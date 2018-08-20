import numpy as np
import matplotlib.pyplot as plt

pi = np.pi


def cal_phase(phi_s, phi, H_phi):
    DW0 = []
    phi0 = []
    phi1 = []
    DW1 = []
    DW2 = phi * np.cos(phi_s) - np.sin(phi) + H_phi
    for i in range(np.size(DW2)):
        i += 1
        if DW2[-i] > 0:
            phi0.append(phi[-i])
            DW0.append(np.sqrt(DW2[-i]))
    for i in range(np.size(DW0)):
        i += 1
        phi1.append(phi0[-i])
        DW1.append(-1 * DW0[-i])
    phi = phi0 + phi1
    DW = DW0 + DW1
    return phi, DW


def main():
    phi_s = -1 * pi / 4
    phi = np.arange(-pi, pi / 2, 0.00001 * pi)
    H_phi = - np.sin(phi_s) + phi_s * np.cos(phi_s)
    phi, DW = cal_phase(phi_s, phi, H_phi)
    phi1 = np.arange(-pi, pi / 2, 0.00001 * pi)
    H_phi1 = - np.sin(phi_s) + phi_s * np.cos(phi_s) + 0.1
    phi1, DW1 = cal_phase(phi_s, phi1, H_phi1)
    phi2 = np.arange(-pi, pi / 6, 0.00001 * pi)
    H_phi2 = - np.sin(phi_s) + phi_s * np.cos(phi_s) - 0.1
    phi2, DW2 = cal_phase(phi_s, phi2, H_phi2)
    phi3 = np.arange(-pi, pi / 6, 0.00001 * pi)
    H_phi3 = - np.sin(phi_s) + phi_s * np.cos(phi_s) - 0.2
    phi3, DW3 = cal_phase(phi_s, phi3, H_phi3)

    fig, ax = plt.subplots()
    plt.plot(phi, DW, phi1, DW1, phi2, DW2, phi3, DW3)
    plt.show()


if __name__ == '__main__':
    main()
