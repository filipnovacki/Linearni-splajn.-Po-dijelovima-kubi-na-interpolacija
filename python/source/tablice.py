import numpy as np


def lin_sin_latex():
    b = 2 * np.pi
    a = 0
    n = 40
    h = (b - a) / n
    print("xi\t yi\t\t xi+1\t\t yi+1\t\t jednadžba \t\t razlika do f(1)")
    print("_________________________________________________________________________________________")
    for i in range(0, n):
        x1 = a + i * h
        y1 = np.sin(x1)
        x2 = a + (i + 1) * h
        y2 = np.sin(x2)
        nagib = (y2 - y1) / (x2 - x1)
        slobodni_clan = nagib * (-x1) + y1

        razlika = nagib * x1 + slobodni_clan - np.sin(1)

        # Priprema za ispis
        slobodni_clan_float = np.asscalar(slobodni_clan)
        slobodni_clan_str = str(format(slobodni_clan_float, '.4f'))

        nagib_str = str(format(np.asscalar(nagib), '.4f'))

        pravac = str("y = " +
                     (nagib_str if nagib < 0 else " " + nagib_str) + "x" +
                     ("+" + slobodni_clan_str if slobodni_clan >= 0 else slobodni_clan_str))

        print(i + 1, "&" + "$" + format(x1, '.4f') + "$" + "&" +
              "$" + format(y1, '.4f') + "$" + "&" +
              "$" + format(x2, '.4f') + "$" + "&" +
              "$" + format(y2, '.4f') + "$" + "&" +
              "$" + pravac.strip(" ") + "$" + "&" +
              "$" + format(razlika, '.2f') + "$" + "\\\\")


def lin_sin_table():
    b = 2 * np.pi
    a = 0
    n = 40
    h = (b - a) / n
    print("xi\t yi\t\t xi+1\t\t yi+1\t\t jednadžba \t\t razlika do f(1)")
    print("_________________________________________________________________________________________")
    for i in range(0, n):
        x1 = a + i * h
        y1 = np.sin(x1)
        x2 = a + (i + 1) * h
        y2 = np.sin(x2)
        nagib = (y2 - y1) / (x2 - x1)
        slobodni_clan = nagib * (-x1) + y1

        razlika = nagib * x1 + slobodni_clan - np.sin(1)

        # Priprema za ispis
        slobodni_clan_float = np.asscalar(slobodni_clan)
        slobodni_clan_str = str(format(slobodni_clan_float, '.4f'))

        nagib_str = str(format(np.asscalar(nagib), '.4f'))

        pravac = str("y = " +
                     (nagib_str if nagib < 0 else " " + nagib_str) + "x" +
                     ("+" + slobodni_clan_str if slobodni_clan >= 0 else slobodni_clan_str))

        print(format(x1, '.4f'), "\t", format(y1, '.4f'), "\t|",
              format(x2, '.4f'), "\t", format(y2, '.4f'), "\t|",
              pravac + "\t|",
              format(razlika, '.2f'))


def lin_razlomak_table():
    b = 5
    a = -5
    n = 40
    h = (b - a) / n
    print("xi\t yi\t\t xi+1\t\t yi+1\t\t jednadžba \t\t razlika do f(1)")
    print("_________________________________________________________________________________________")
    for i in range(0, n):
        x1 = a + i * h
        y1 = 1 / (x1 ** 2 + 1)
        x2 = a + (i + 1) * h
        y2 = 1 / (x2 ** 2 + 1)
        nagib = (y2 - y1) / (x2 - x1)
        slobodni_clan = nagib * (-x1) + y1

        razlika = nagib * x1 + slobodni_clan - (1 / (1.2 ** 2 + 1))

        # Priprema za ispis
        slobodni_clan_float = slobodni_clan
        slobodni_clan_str = str(format(slobodni_clan_float, '.4f'))

        nagib_str = str(format(nagib, '.4f'))

        pravac = str("y = " +
                     (nagib_str if nagib < 0 else " " + nagib_str) + "x" +
                     ("+" + slobodni_clan_str if slobodni_clan >= 0 else slobodni_clan_str))

        print(format(x1, '.3f'), "\t", format(y1, '.4f'), "\t|",
              format(x2, '.4f'), "\t", format(y2, '.4f'), "\t|",
              pravac + "\t|",
              format(razlika, '.2f'))


def lin_razlomak_latex():
    b = 5
    a = -5
    n = 40
    h = (b - a) / n
    print("xi\t yi\t\t xi+1\t\t yi+1\t\t jednadžba \t\t razlika do f(1)")
    print("_________________________________________________________________________________________")
    for i in range(0, n):
        x1 = a + i * h
        y1 = 1 / (x1 ** 2 + 1)
        x2 = a + (i + 1) * h
        y2 = 1 / (x2 ** 2 + 1)
        nagib = (y2 - y1) / (x2 - x1)
        slobodni_clan = nagib * (-x1) + y1

        razlika = nagib * x1 + slobodni_clan - (1 / (1.2 ** 2 + 1))

        # Priprema za ispis
        slobodni_clan_float = slobodni_clan
        slobodni_clan_str = str(format(slobodni_clan_float, '.4f'))

        nagib_str = str(format(nagib, '.4f'))

        pravac = str("y = " +
                     (nagib_str if nagib < 0 else " " + nagib_str) + "x" +
                     ("+" + slobodni_clan_str if slobodni_clan >= 0 else slobodni_clan_str))

        # print(format(x1, '.3f'), "\t", format(y1, '.4f'), "\t|",
        #       format(x2, '.4f'), "\t", format(y2, '.4f'), "\t|",
        #       pravac + "\t|",
        #       format(razlika, '.2f'))

        print(i + 1, "&" + "$" + format(x1, '.2f') + "$" + "&" +
              "$" + format(y1, '.4f') + "$" + "&" +
              "$" + format(x2, '.2f') + "$" + "&" +
              "$" + format(y2, '.4f') + "$" + "&" +
              "$" + pravac.strip(" ") + "$" + "&" +
              "$" + format(razlika, '.2f') + "$" + "\\\\")


def kub_sin_table():
    b = 2 * np.pi
    a = 0
    n = 40
    h = (b - a) / n

    print("c0\t\t c1\t\t\t c2\t\t\t c3\t\t razlika do f(1)")
    print("_________________________________________________________________________________________")
    for i in range(0, n):
        x = a + i * h
        x0=a+(i-1)*h
        c0 = np.sin(x)
        c1 = np.cos(x)
        c2 = -np.sin(x) / 2
        c3 = -np.cos(x) / 6

        fx=np.sin(1)
        razlika = (c3 * fx ** 3 + c2 * fx ** 2 + c1 * fx + c0) - fx

        print(format(c0, '.4f'), '\t',
              format(c1, '.4f'), '\t',
              format(c2, '.4f'), '\t',
              format(c3, '.4f'), '\t',
              format(razlika, '.4f'))


def kub_sin_latex():
    b = 2 * np.pi
    a = 0
    n = 40
    h = (b - a) / n

    print("c0\t\t c1\t\t\t c2\t\t\t c3\t\t razlika do f(1)")
    print("_________________________________________________________________________________________")
    for i in range(0, n):
        x = a + i * h
        x0=a+(i-1)*h
        c0 = np.sin(x)
        c1 = np.cos(x)
        c2 = -np.sin(x) / 2
        c3 = -np.cos(x) / 6

        fx=np.sin(1)
        razlika = (c3 * fx ** 3 + c2 * fx ** 2 + c1 * fx + c0) - fx

        print(format(c0, '.4f'), '&',
              format(c1, '.4f'), '&',
              format(c2, '.4f'), '&',
              format(c3, '.4f'), '&',
              format(razlika, '.4f'), "\\\\")


def kub_drugi_table():
    print("c0\tc1\t\tc2\t\tc3\t\tRazlika")
    tocka = 1/(1.2**2+1)
    #print("Funkcija interpolacije\t\tRazlika f(1)-interpolacija")
    print("............................................................................")
    for k in range(-20,20):
        x = 1 / 4
        # Racunanje koeficijenata:
        c0 = 1 / ((k * x) ** 2 + 1)
        c1 = -(2 * (k * x)) / (((k * x) ** 2 + 1) ** 2)
        c2 = (2 * (3 * (k * x) ** 2 - 1)) / (((k * x) ** 2 + 1) ** 3)
        c3 = -(24 * k * x * ((k * x) ** 2 - 1)) / (((k * x) ** 2 + 1) ** 4)

        razlika = tocka - (c0 + c1 * (1.2 - k * x) + c2 * (1.2 - k * x) ** 2 + c3 * (1.2 - k * x) ** 3)

        #print(format(c0,'.3f')+format(c1, '.3f') if c1<0 else ("+" + format(c1,'.3f')) + '(x'+ str(x*(k-1)) if (x*(k-1)<0) else ('-'+str(x*(k-1))) + ')'+format(c2, '.3f') if c2<0 else ("+" + format(c2,'.3f')) + '(x'+ str(x*(k-1)) if x*(k-1)<0 else ('-'+str(x*(k-1))) + ')^2'+format(c3, '.3f') if c3 < 0 else ("+" + format(c3, '.3f')) + '(x' + str(x * (k - 1)) if x * (k - 1) < 0 else ('-' + str(x * (k - 1))) + ')^3')
        print(format(c0, '.3f'), " \t", format(c1, '.3f'), " \t", format(c2, '.3f'), " \t", format(c3, '.3f'),"\t", razlika)


def kub_drugi_latex():
    print("c0&c1&c2&c3&Razlika")
    tocka = 1 / (1.2 ** 2 + 1)
    # print("Funkcija interpolacije\t\tRazlika f(1)-interpolacija")
    for k in range(-20, 20):
        x = 1 / 4
        # Racunanje koeficijenata:
        c0 = 1 / ((k * x) ** 2 + 1)
        c1 = -(2 * (k * x)) / (((k * x) ** 2 + 1) ** 2)
        c2 = (2 * (3 * (k * x) ** 2 - 1)) / (((k * x) ** 2 + 1) ** 3)
        c3 = -(24 * k * x * ((k * x) ** 2 - 1)) / (((k * x) ** 2 + 1) ** 4)

        razlika = tocka - (c0 + c1 * (1.2 - k * x) + c2 * (1.2 - k * x) ** 2 + c3 * (1.2 - k * x) ** 3)

        print(format(c0, '.3f'), " &", format(c1, '.3f'), " &", format(c2, '.3f'), " &", format(c3, '.3f'), "&",
              format(razlika, '.3f'),"\\\\")

def meni(odabir):
    if odabir == 2:
        lin_sin_latex()
        pass
    elif odabir == 1:
        lin_sin_table()
        pass
    elif odabir == 3:
        lin_razlomak_table()
        pass
    elif odabir == 4:
        lin_razlomak_latex()
        pass
    elif odabir == 5:
        kub_sin_table()
        pass
    elif odabir == 6:
        kub_sin_latex()
        pass
    elif odabir == 7:
        kub_drugi_table()
        pass
    elif odabir == 8:
        kub_drugi_latex()
        pass
    elif odabir == 9:
        pass
    elif odabir == 10:
        pass
    elif odabir == 11:
        pass
    elif odabir == 12:
        pass


unos = 1
while unos != 0:
    print("Dobrodosli u programski dio rješenja OPM-a")
    print("Unesite koju funkciju želite izvršiti:")
    print("\nLINEARNA INTERPOLACIJA:"
          "\n----------------------"
          "\nRacunanje tablice za funkciju f(x)=sin(x)"
          "\n   1. plain text tablica"
          "\n   2. LaTeX export tablica"
          "\nRacunanje tablica za funkciju f(x)=1/(x^2+1)"
          "\n   3. plain text tablica"
          "\n   4. LaTeX export tablica"
          "\n\nKUBICNA INTERPOLACIJA:"
          "\n----------------------"
          "\nRacucanje tablica za funkciju f(x)=sin(x)"
          "\n   5. plain text tablica"
          "\n   6. LaTeX export tablica"
          "\nRacunanje tablica za funkciju f(x)=1/(x^2+1)"
          "\n   7. plain text tablica"
          "\n   8. LaTeX export tablica"
          # "\n\nGENERIRANJE SLIKA"
          # "\n-----------------"
          # "\nLinearna interpolacija (40 slika):"
          # "\n   9. prikaz na nacin da se vidi samo isjecak funkcije"
          # "\n   10. prikaz na nacin da se vidi cijela funkcija"
          # "\nKubicna interpolacija (40 slika):"
          # "\n   11. prikaz na nacin da se vidi samo isjecak funkcije"
          # "\n   12. prikaz na nacin da se vidi cijela funkcija"
          )
    unos = int(input("Vas odabir: "))
    meni(unos)
