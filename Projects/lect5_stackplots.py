import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]

sleeping = [6,6,6,6,6,6,5]
eating = [6,6,6,6,6,6,7]
working = [8,6,6,6,6,6,11]
playing = [4,6,6,6,6,6,1]

plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','b'])









plt.xlabel('x')
plt.ylabel('y')

plt.title('Lect 4')

plt.legend()

plt.show()