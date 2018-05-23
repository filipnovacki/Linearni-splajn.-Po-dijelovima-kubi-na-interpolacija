import numpy as np
import matplotlib.pyplot as plt


def crtaj_sin():
    pass
    for k in range(0,40):

        # racunanje faktora tako da se zadovolji jednadzba
        # c0 + c1(x-xk-1)**1+...+cn(x-xk-1)**n

        # Trenutna tocka
        x = np.pi/20

        # Racunanje koeficijenata
        c0 = np.sin(k*x)
        c1 = np.cos(k*x)
        c2 = -np.sin(k*x)
        c3 = -np.cos(k*x)

        ax = plt.subplot(111)

        # Crtanje glavne funkcije np.arange(start, stop, step)
        domena_funkcije = np.arange(0, 2*np.pi, 0.01)
        kodomena_funkcije = np.sin(domena_funkcije)

        # Crtanje interpolacije

        domena_interpolacije = np.arange(0, 2*np.pi, 0.01)
        kodomena_interpolacije = c0 + c1*(domena_interpolacije-k*x)+ (c2*(domena_interpolacije-k*x)**2)/2 + (c3*(domena_interpolacije-k*x)**3)/6

        # Zavrsna faza prikaza
        ax.plot(domena_funkcije, kodomena_funkcije)
        ax.plot(domena_interpolacije, kodomena_interpolacije)

        # Ogranicenje na min. y
        plt.ylim(-1,1)

        # Prikaz cijelog grafa
        plt.savefig('slike/kubicna_interpolacija/sinus/slika'+str(k)+'.eps', format='eps')
        plt.show()


# Drugi je kolokvijalni naziv za funkciju g(x)=1/(x**2+1).
# Razlog tomu je što je nespretno imati takav naziv metode u programskom jeziku
def crtaj_drugi():
    for k in range(-20, 20):
        # racunanje faktora tako da se zadovolji jednadzba
        # c0 + c1(x-xk-1)**1+...+cn(x-xk-1)**n

        # h (delta x između dviju točaka interpolacije)
        x = 1/4

        # Racunanje koeficijenata
        c0 = 1/((k*x)**2+1)
        c1 = -(2*(k * x))/(((k*x)**2+1)**2)
        c2 = (2*(3*(k*x)**2-1))/(((k*x)**2+1)**3)
        c3 = -(24*k*x*((k*x)**2-1))/(((k*x)**2+1)**4)

        ax = plt.subplot(111)

        # Crtanje glavne funkcije np.arange(start, stop, step)
        domena_funkcije = np.arange(-5, 5, 0.01)
        kodomena_funkcije = 1/(domena_funkcije**2+1)

        # Crtanje interpolacije

        domena_interpolacije = np.arange(-5, 5, 0.01)
        kodomena_interpolacije = c0 + c1 * (domena_interpolacije - k * x) + c2 * (
                    domena_interpolacije - k * x) ** 2 + c3 * (domena_interpolacije - k * x) ** 3

        # Zavrsna faza prikaza
        ax.plot(domena_funkcije, kodomena_funkcije)
        ax.plot(domena_interpolacije, kodomena_interpolacije)

        # Ogranicenje na min. y
        plt.ylim(0, 1)

        # Prikaz cijelog grafa
        plt.savefig('slike/kubicna_interpolacija/drugi/slika' + str(k) + '.eps', format='eps')
        plt.show()


#Funkcija za odabir funkcije
def meni(odabir):
    if odabir==1:
        crtaj_sin()
    if odabir==2:
        crtaj_drugi()


print("meni")
print("1. crtanje slike za sin(x)")
print("2. crtanje slike za drugi zadatak")

meni(int(input("Vas odabir?")))
