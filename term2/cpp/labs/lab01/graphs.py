import matplotlib.pyplot as plt

# Strategy
sizes_strategy = []
strategy_a = []
strategy_b = []
strategy_c = []

with open('data/const_data_strategy.txt', 'r') as f:
  lines = f.readlines()[1:] 
  for line in lines:
    data = line.split()
    sizes_strategy.append(int(data[0]))
    strategy_a.append(int(data[1]))
    strategy_b.append(int(data[2]))
    strategy_c.append(int(data[3]))

fig, axes = plt.subplots(3, 1, figsize=(8, 10))  

# Strategy A
axes[0].plot(sizes_strategy, strategy_a, label='StrategyA', color='blue')
axes[0].set_xlabel('Sizes')
axes[0].set_ylabel('Time, ms')
axes[0].set_title('StrategyA Time Complexity')
axes[0].legend()
axes[0].grid(True)

# Strategy B
axes[1].plot(sizes_strategy, strategy_b, label='StrategyB', color='green')
axes[1].set_xlabel('Sizes')
axes[1].set_ylabel('Time')
axes[1].set_title('StrategyB Time Complexity')
axes[1].legend()
axes[1].grid(True)

# Strategy C
axes[2].plot(sizes_strategy, strategy_c, label='StrategyC', color='red')
axes[2].set_xlabel('Sizes')
axes[2].set_ylabel('Time')
axes[2].set_title('StrategyC Time Complexity')
axes[2].legend()
axes[2].grid(True)

plt.tight_layout()
plt.savefig('graph/strategy_graph.png')

# Search
sizes_search = []
linear_avg = []
linear_worst = []
binary_avg = []
binary_worst = []

with open('data/const_data_search.txt', 'r') as f:
  lines = f.readlines()[1:]  # Пропускаем заголовок
  for line in lines:
    data_search = line.split()
    sizes_search.append(int(data_search[0]))
    linear_avg.append(int(data_search[1]))
    linear_worst.append(int(data_search[2]))
    binary_avg.append(int(data_search[3]))
    binary_worst.append(int(data_search[4]))

fig, axes = plt.subplots(2, 1, figsize=(8, 10))  

axes[0].plot(sizes_search, linear_avg, label='Linear_Avg', color='blue')
axes[0].plot(sizes_search, [i * (linear_worst[len(linear_worst) - 1] / sizes_search[len(linear_worst) - 1]) for i in sizes_search], label='O(n)', color='gray', linestyle='--')
axes[0].set_xlabel('Sizes')
axes[0].set_ylabel('Time')
axes[0].set_title('Linear Average Time Complexity')
axes[0].legend()
axes[0].grid(True)

axes[1].plot(sizes_search, linear_worst, label='Linear_Worst', color='red')
axes[1].plot(sizes_search, [i * (linear_worst[len(linear_worst) - 1] / sizes_search[len(linear_worst) - 1]) for i in sizes_search], label='O(n)', color='gray', linestyle='--')
axes[1].set_xlabel('Sizes')
axes[1].set_ylabel('Time')
axes[1].set_title('Linear Worst Time Complexity')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.savefig('graph/linear_graph.png')

fig, axes = plt.subplots(2, 1, figsize=(8, 10))  

axes[0].plot(sizes_search, binary_avg, label='Binary_Avg', color='green')
axes[0].set_xlabel('Sizes')
axes[0].set_ylabel('Time')
axes[0].set_title('Binary Average Time Complexity')
axes[0].legend()
axes[0].grid(True)

axes[1].plot(sizes_search, binary_worst, label='Binary_Worst', color='orange')
axes[1].set_xlabel('Sizes')
axes[1].set_ylabel('Time')
axes[1].set_title('Binary Worst Time Complexity')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.savefig('graph/binary_graph.png')


# Pair
sizes_pair = []
pair_linear_avg = []
pair_linear_worst = []
pair_binary_avg = []
pair_binary_worst = []

with open('data/const_data_pair.txt', 'r') as f:
  lines = f.readlines()[1:]  # Пропускаем заголовок
  for line in lines:
    data_pair = line.split()
    if len(data_pair) < 5:
      continue
    sizes_pair.append(int(data_pair[0]))
    pair_linear_avg.append(int(data_pair[1]))
    pair_linear_worst.append(int(data_pair[2]))
    pair_binary_avg.append(int(data_pair[3]))
    pair_binary_worst.append(int(data_pair[4]))


fig, axes = plt.subplots(2, 1, figsize=(8, 12))  

axes[0].plot(sizes_pair, pair_linear_avg, label='Pair_Linear_Avg', color='blue')
axes[0].set_xlabel('Sizes')
axes[0].set_ylabel('Time')
axes[0].set_title('Pair Linear Average Time Complexity')
axes[0].legend()
axes[0].grid(True)

axes[1].plot(sizes_pair, pair_linear_worst, label='Pair_Linear_Worst', color='red')
axes[1].set_xlabel('Sizes')
axes[1].set_ylabel('Time')
axes[1].set_title('Pair Linear Worst Time Complexity')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.savefig('graph/pair_linear_graph.png')

fig, axes = plt.subplots(2, 1, figsize=(8, 10))  

axes[0].plot(sizes_pair, pair_binary_avg, label='Pair_Binary_Avg', color='green')
axes[0].set_xlabel('Sizes')
axes[0].set_ylabel('Time')
axes[0].set_title('Pair Binary Average Time Complexity')
axes[0].legend()
axes[0].grid(True)

axes[1].plot(sizes_pair, pair_binary_worst, label='Pair_Binary_Worst', color='orange')
axes[1].set_xlabel('Sizes')
axes[1].set_ylabel('Time')
axes[1].set_title('Pair Binary Worst Time Complexity')
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.savefig('graph/pair_binary_graph.png')

