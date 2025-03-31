import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
data = pd.read_csv('data/results_static.csv')

# Графики времени сортировок
plt.figure(figsize=(10, 6))

plt.plot(data['Size'], data['ShakerSortTime'], label='ShakerSort', marker='o')
plt.plot(data['Size'], data['CombSortTime'], label='CombSort', marker='o')
plt.plot(data['Size'], data['ShellSortStandardTime'], label='ShellSort (Standard)', marker='o')
plt.plot(data['Size'], data['ShellSortFibTime'], label='ShellSort (Fibonacci Reversed)', marker='o')
plt.plot(data['Size'], data['ShellSortHibbardTime'], label='ShellSort (Hibbard)', marker='o')

plt.xlabel('Size of Vector')
plt.ylabel('Time (ms)')
plt.title('Sorting Algorithms Time Complexity')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("graph/time.png")

# Графики количества перестановок
plt.figure(figsize=(10, 6))

plt.plot(data['Size'], data['ShakerSortSwaps'], label='ShakerSort', marker='o')
plt.plot(data['Size'], data['CombSortSwaps'], label='CombSort', marker='o')
plt.plot(data['Size'], data['ShellSortStandardSwaps'], label='ShellSort (Standard)', marker='o')
plt.plot(data['Size'], data['ShellSortFibSwaps'], label='ShellSort (Fibonacci Reversed)', marker='o')
plt.plot(data['Size'], data['ShellSortHibbardSwaps'], label='ShellSort (Hibbard)', marker='o')

plt.xlabel('Size of Vector')
plt.ylabel('Number of Swaps')
plt.title('Sorting Algorithms Swap Count')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("graph/swap.png")
