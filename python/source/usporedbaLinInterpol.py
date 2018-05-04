import matplotlib.pyplot as plt
import numpy as np


# Zadana je funkcija f(x)=sin(x) na segmentu [0, 2pi]
# Primijenite algoritam iz zadatka 3 da biste pronasli
# linearni splajn funkcije f i to za n = 1, 2, ,..., 40
# Nacrtajte te linearne splajnove
# Koliko je dobra aproksimacija
# Izračunati grešku interpolacije u točki x=1

def crtaj_sin_interpolaciju():
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    # plt.figure(figsize=(14,14))
    plt.grid()
    # plt.title('Usporedba')

    ax = plt.subplot(111)

    opseg_detaljan = np.arange(0, 2 * np.pi, 0.01)
    vrijednosti_detaljne = np.sin(opseg_detaljan)
    plt.plot(opseg_detaljan, vrijednosti_detaljne, label="Stvarna funkcija")

    # Opseg od 0 do 2pi za n=40
    opseg = np.arange(0, 2 * np.pi, 2 * np.pi / 40)
    vrijednosti = np.sin(opseg)
    plt.plot(opseg, vrijednosti)

    plt.savefig('slike/usporedbaLinearneInterpolacijeSin.png', dpi=450)
    plt.show()


crtaj_sin_interpolaciju()
