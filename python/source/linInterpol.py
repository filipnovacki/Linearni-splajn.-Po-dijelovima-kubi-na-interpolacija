import matplotlib.pyplot as plt
import numpy as np


ax = plt.subplot(111)


def crtaj_sin():
    for i in range(0,40):
        # Brise canvas tako da se moze crtati od pocetka
        #ax.clear()
        const = 2 * np.pi / 40
        # Aspect ratio osi je jednak
        #ax.set_aspect(aspect="equal")
        plt.ylim(-1,1)
        ax=plt.subplot(111)

        #Koeficijenti
        x0=i*const
        x1=(i+1)*const

        y0=np.sin(x0)
        y1=np.sin(x1)

        # Crtanje glavne funkcije np.arange(start, stop, step)
        domena_funkcije = np.arange(0, 2 * np.pi, 0.01)
        kodomena_funkcije = np.sin(domena_funkcije)

        # Crtanje interpolacije
        domena_interpolacije = np.arange(0, 2 * np.pi, 0.01)
        kodomena_interpolacije = ((y1-y0)/(x1-x0))*(domena_interpolacije-x0)+y0

        # Zavrsna faza prikaza
        ax.plot(domena_funkcije, kodomena_funkcije)
        ax.plot(domena_interpolacije, kodomena_interpolacije)

        plt.savefig('slike/linearna_interpolacija/sinus/slika' + str(i) + '.eps', format='eps')
        plt.show()

def crtaj_drugi():
    for i in range(-20,20):
        const = 1/4
        plt.ylim(-1,1)
        ax=plt.subplot(111)

        #Koeficijenti
        x0=i*const
        x1=(i+1)*const

        y0=1 / (np.square(x0) + 1)
        y1=1 / (np.square(x1) + 1)

        # Crtanje glavne funkcije np.arange(start, stop, step)
        domena_funkcije = np.arange(-5, 5, 0.01)
        kodomena_funkcije = 1 / (np.square(domena_funkcije) + 1)

        # Crtanje interpolacije
        domena_interpolacije = np.arange(-5, 5, 0.01)
        kodomena_interpolacije = ((y1-y0)/(x1-x0))*(domena_interpolacije-x0)+y0

        # Zavrsna faza prikaza
        ax.plot(domena_funkcije, kodomena_funkcije)
        ax.plot(domena_interpolacije, kodomena_interpolacije)

        plt.savefig('slike/linearna_interpolacija/drugi/slika' + str(i) + '.eps', format='eps')
        plt.show()


# Funkcija za odabir funkcije
def meni(odabir):
    if odabir==1:
        crtaj_sin()
    if odabir==2:
        crtaj_drugi()


print("meni")
print("1. crtanje slika za sin(x)")
print("2. crtanje slika za drugi zadatak")

meni(int(input("Vas odabir?")))