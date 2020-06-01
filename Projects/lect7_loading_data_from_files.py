import matplotlib.pyplot as plt
import numpy as np

# -------Via CSV
# import csv
#
# x=[]
# y=[]
#
# with open('sample_csv.txt','r') as csvfile:
#     plots = csv.reader(csvfile,delimiter=',')
#     for row in plots:
#         x.append(int(row[0]))
#         y.append(int(row[1]))
# ------------------------------------

x,y = np.loadtxt('sample_csv.txt',delimiter=',',unpack=True)
plt.plot(x,y,label='From sample csv')



plt.xlabel('x')
plt.ylabel('y')

plt.title('Lect 7')

plt.legend()

plt.show()