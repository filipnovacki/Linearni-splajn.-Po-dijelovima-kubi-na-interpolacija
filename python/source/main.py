import numpy as np


def linearni_prvi():
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

        # print(i+1, "&" + "$" + format(x1, '.4f') + "$" + "&" +
        #       "$" + format(y1, '.4f') + "$" + "&" +
        #       "$" + format(x2, '.4f') + "$" + "&" +
        #       "$" + format(y2, '.4f') + "$" + "&" +
        #       "$" + pravac.strip(" ") + "$" + "&" +
        #       "$" + format(razlika, '.2f') + "$" + "\\\\")


def linearni_drugi():
    b = 5
    a = -5
    n = 40
    h = (b - a) / n
    print("xi\t yi\t\t xi+1\t\t yi+1\t\t jednadžba \t\t razlika do f(1)")
    print("_________________________________________________________________________________________")
    for i in range(0, n):
        x1 = a + i * h
        y1 = 1/(x1**2+1)
        x2 = a + (i + 1) * h
        y2 = 1/(x2**2+1)
        nagib = (y2 - y1) / (x2 - x1)
        slobodni_clan = nagib * (-x1) + y1

        razlika = nagib * x1 + slobodni_clan - (1/(1.2**2+1))

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

        print(i+1, "&" + "$" + format(x1, '.2f') + "$" + "&" +
              "$" + format(y1, '.4f') + "$" + "&" +
              "$" + format(x2, '.2f') + "$" + "&" +
              "$" + format(y2, '.4f') + "$" + "&" +
              "$" + pravac.strip(" ") + "$" + "&" +
              "$" + format(razlika, '.2f') + "$" + "\\\\")


def kubicni_drugi():
    pass


def kubicni_prvi():
    pass


def meni(odabir):
    if odabir == 4:
        print("Odabran je cetvrti zadatak")
        linearni_prvi()
    elif odabir == 5:
        linearni_drugi()
    elif odabir == 9:
        kubicni_prvi()
    elif odabir == 10:
        kubicni_drugi()


print("Dobrodosli u programski dio rješenja OPM-a")
print("Unesite broj zadatka za kojeg želite rješenje:")
print("Mogući odabiri su: 4, 5, 9, 10")

meni(int(input("Vas odabir: ")))
