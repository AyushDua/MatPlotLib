import matplotlib.pyplot as plt

slices = [7,8,5,4]
activities = ['sleeping','working','eating','playing']
colors = ['c','m','r','b']

plt.pie(
    slices,
    labels=activities,
    colors=colors,
    startangle=90,
    shadow=True,
    explode=(0,0.1,0,0),
    autopct='%1.2f%%'
)




# plt.xlabel('x')
# plt.ylabel('y')

plt.title('Lect 6')

# plt.legend()

plt.show()