import matplotlib.pyplot as plt
import numpy as np

plt.grid()
ax = plt.subplot(111)
const = 2 * np.pi / 40
i = 0
while (i <= 40):
    # Brise canvas tako da se moze crtati od pocetka
    ax.clear()

    # Aspect ratio osi je jednak
    ax.set_aspect(aspect="equal")

    # Racunanje linearne interpolacije
    opseg = np.arange(-0.00001 + i * const, (i + 1) * const, const)
    vrijednosti = np.sin(opseg)
    plt.plot(opseg, vrijednosti)

    # Racunanje kvaziprave funkcije
    opseg_detaljan = np.arange(-0.00001 + i * const, (i + 1) * const, 0.0001)
    vrijednosti_detaljne = np.sin(opseg_detaljan)
    plt.plot(opseg_detaljan, vrijednosti_detaljne)

    plt.savefig('slike/usporedba4_' + str(i) + '.png', dpi=150)
    i += 1

const = 11/40
i = 0
while i <= 40:
    # Brise canvas tako da se moze crtati od pocetka
    ax.clear()

    # Aspect ratio osi je jednak
    ax.set_aspect(aspect="num")

    # Racunanje linearne interpolacije
    opseg = np.arange(-5.00001 + i * const, (i + 1) * const, const)
    vrijednosti = 1/(np.square(opseg)+1)
    plt.plot(opseg, vrijednosti)

    # Racunanje kvaziprave funkcije
    opseg_detaljan = np.arange(-5.00001 + i * const, (i + 1) * const, 0.0001)
    vrijednosti_detaljne = 1/(np.square(opseg_detaljan)+1)
    plt.plot(opseg_detaljan, vrijednosti_detaljne)

    plt.savefig('slike/usporedba5_' + str(i) + '.png', dpi=150)
    i += 1
