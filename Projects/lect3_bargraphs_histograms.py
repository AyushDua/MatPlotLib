import matplotlib.pyplot as plt
# Bar Graph Code
# x1 = [2, 4, 6, 8, 10, 12]
# y1 = [2, 4, 6, 8, 10, 12]
#
# x2 = [1, 3, 5, 7, 9, 11]
# y2 = [3, 6, 9, 12, 15, 18]
#
# plt.bar(x1, y1, label='Bar1', color='red')
# plt.bar(x2, y2, label='Bar2', color='cyan')
# ------------Bar Graph Code Ends----------------

# Histogram Code
ages = [10,20,15,25,1,4,85,95,63,78,45,21,98,110,120,129,130,101,99,12,15,18,25,26,37,47,59,68,65,77,87,99,100,98,107,111,17,19,17]
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(ages, bins, histtype='bar', rwidth=0.8, label='Number Of PPL')

# -------------Histogram Code Ends---------------------






plt.xlabel('x')
plt.ylabel('y')

plt.title('Lect 3')

plt.legend()

plt.show()
