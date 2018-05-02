import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])

plt.subplot(211)
plt.plot(range(12))
plt.subplot(212, facecolor='y')

plt.plot(range(12))
plt.subplot(212, facecolor='g')


plt.show()