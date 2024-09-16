import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_table = pd.read_csv('data.csv')
print(data_table)

data_20 = data_table.to_numpy().flatten()

values_10 = np.array([i for i in range(3, 24)] + [25, 27, 28])
counts_10 = np.array([1, 2, 1, 2, 5, 8, 17, 34, 32,
                      40, 38, 43, 33, 31, 36, 28, 12, 18,
                      10, 4, 1, 1, 2, 1])
data_10 = []
for i in range(len(values_10)):
    data_10 += [values_10[i]] * counts_10[i]
data_10 = np.array(data_10)

hist_10 = pd.DataFrame(np.vstack((values_10, counts_10)))
print(hist_10)

def to_latex(s):
    return ' & '.join([*map(str, list(s))])

values_20, counts_20 = np.unique(data_20, return_counts=True)

data_40 = np.empty(100, dtype=int)
for i in range(100):
    data_40[i] = data_20[2*i] + data_20[2*i + 1]
values_40, counts_40 = np.unique(data_40, return_counts=True)
print(values_40, counts_40)

a, b = 22, 33
print(to_latex(values_40[a:b]))
print(to_latex(counts_40[a:b]))
print(to_latex(counts_40[a:b]/100))

print(np.sum(data_40)/100)

print(np.sum(data_10)/400)

fig, ax1 = plt.subplots()
fig.set_figheight(16)
fig.set_figwidth(20)

color = 'tab:red'
ax1.set_xlabel('$n$  (10с)', fontsize=30, color=color)
ax1.set_ylabel(r'$\omega$', fontsize=30)
ax1.hist(data_10, np.arange(0, 31), alpha=0.5, density=True, label='10с', color=color)

ax1.tick_params(axis='x', labelcolor=color,  labelsize=30)
ax1.tick_params(axis='y', labelcolor='#000000',  labelsize=30)
plt.legend(loc='upper left', fontsize=30)

color = 'tab:blue'
ax2 = ax1.twiny()
ax2.set_xlabel('$n$  (40с)', fontsize=30, color=color)

ax2.hist(data_40, np.arange(0, 121), alpha=0.5, density=True, label='40с')
ax2.tick_params(axis='x', labelcolor=color, labelsize=30)
fig.tight_layout()
plt.legend(loc='upper right', fontsize=30)
plt.savefig('histogram.png')
plt.show()



