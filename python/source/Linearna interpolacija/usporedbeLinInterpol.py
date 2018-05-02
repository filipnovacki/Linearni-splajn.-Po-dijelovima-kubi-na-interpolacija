import matplotlib.pyplot as plt
import numpy as np

plt.grid()
ax = plt.subplot(111)
const = 2*np.pi/40
i=1
while(i<=40):
    ax.clear()

    opseg = np.arange(-0.00001 + i*const, (i+1)*const, 2*np.pi/40)
    vrijednosti = np.sin(opseg)
    plt.plot(opseg, vrijednosti)

    opseg_detaljan = np.arange(-0.00001 + i*const, (i+1)*const, 0.0001)
    vrijednosti_detaljne = np.sin(opseg_detaljan)
    plt.plot(opseg_detaljan, vrijednosti_detaljne)
    #plt.show()

    plt.savefig('slike/usporedba'+str(i)+'.png')
    i+=1
