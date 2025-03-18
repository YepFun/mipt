import numpy as np
import math
import matplotlib.pyplot as plt

graph = "data/graph.txt"
with open(graph) as f:
  lines = f.readlines()

T_values = []
h_values = []

for line in lines:
  T_values.append(line.strip().split()[0])
  data = line.split()[1:6]
  h_sum = 0
  for i in range(len(data)):
    h_sum += int(data[i])
  h_values.append(h_sum / len(data))

print(*T_values)
print(*h_values)


k = 785.0 * 9.81 * 0.2
ek = 5.0 / 785.0
P_values = []
eP_values = []
dP_values = []

l = (1.1 * 1e-3) / 4
s_values = []
es_values = []
ds_values = []

for i in range(len(h_values)):
  h = h_values[i]
  h *= 1e-3
  P_values.append(k * h)
  eP_values.append(math.sqrt(ek * ek + 1e-6/(h * h)))
  dP_values.append(k * h * math.sqrt(ek * ek + 1e-6/(h * h)))
  s_values.append(k * h * l)
  es_values.append(math.sqrt(ek * ek + 1e-6/(h * h) + (1/11)*(1/11)/16.0))
  ds_values.append(k * h * l * math.sqrt(ek * ek + 1e-6/(h * h) + (1/11)*(1/11)/16.0))

for h in range(len(P_values)):
  print(P_values[h], dP_values[h], eP_values[h], "|", s_values[h], ds_values[h], es_values[h])

# Построение графика
plt.scatter(T_values, h_values, marker='o', color='b', label='h(T)')

# Оформление
plt.xlabel("Температура T")
plt.ylabel("Значение h")
plt.title("Зависимость h от T")
plt.legend()
plt.tight_layout()
plt.grid(True)

# Показать график
plt.savefig("images/graph0.png")
