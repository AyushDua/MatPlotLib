import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]
y = [5,6,8,7,4,1]

plt.scatter(x,y,label='scplt',color='blue',marker='*')




plt.xlabel('x')
plt.ylabel('y')

plt.title('Lect 4')

plt.legend()

plt.show()
