import matplotlib.pyplot as plt
import numpy as np

x = 5
y = 6

# Brojevi od 0 do 2 jednako distribuirani, s razmakom od 0.1, ovdje predstavljaju x os
t = np.arange(0.0, 2.0, 0.01)

# s je rezultat funkcije sin 2pi*t, a ovdje predstavlja y os
s = 1 + np.sin(2 * np.pi * t)


fig, ax = plt.subplots()
ax.plot(t, s)

# imenovanje osi i naziv grafa
ax.set(xlabel='vrijeme (s)',
       ylabel='voltage (mV)',
       title='Ovo je jednostavno')

# Mreza bitnijih brojeva u koordinatnom sustavu
ax.grid()

plt.show()



