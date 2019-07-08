import matplotlib.pyplot as plt


xYear = [1960, 1970, 1980, 1990, 2000, 2010, 2016]
pop_latvia = [2.1, 2.4, 2.5, 2.7, 2.4, 2.1, 1.9]
pop_lithuania = [2.7, 3.1, 3.4, 3.7, 3.5, 3.1, 2.8]
pop_estonia = [1.2, 1.3, 1.5, 1.56, 1.4, 1.3, 1.3]
fig: object = plt.figure()

plt.plot(xYear, pop_latvia, color='red', label='Latvia')
plt.plot(xYear, pop_lithuania, color='g', label='Lithuania')
plt.plot(xYear, pop_estonia, color='blue', label='Estonia')
#function to display lables with position on left top corner
plt.legend(loc='upper left')

plt.xlabel('Year')
plt.ylabel('Population in million')
plt.title('Lithuania, Latvia, Estonia Population till 2016')
plt.xticks([1960, 1970, 1980, 1990, 2000, 2010, 2016])

plt.yticks([1, 2, 3, 4],
           ['0', '1M', '2M', '3M', '4M'])

plt.show()
fig.savefig('population_baltic.png')

