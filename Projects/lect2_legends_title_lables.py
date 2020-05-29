import matplotlib.pyplot as plt

x1 = [1, 2, 3, 4]
y1 = [2, 4, 6, 8]

x2 = [1, 2, 3, 4]
y2 = [3, 6, 9, 12]

plt.plot(x1, y1, label='Line1')
plt.plot(x2, y2, label='Line2')

plt.xlabel('Values')
plt.ylabel('Values * Factor')

plt.suptitle('Hola')
plt.title('My Second Graph')

plt.legend()

plt.show()
