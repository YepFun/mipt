import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Путь к файлу
file_path = "data/data.xlsx"

# Загружаем все листы
xls = pd.ExcelFile(file_path)
sheets = xls.sheet_names

# Создаем график
plt.figure(figsize=(8, 6))

# Цвета для разных листов
colors = ['b', 'g', 'r', 'c', 'm']

for sheet, color in zip(sheets, colors):
    df = xls.parse(sheet)
    plt.scatter(df['t (s)'], df['V (mV)'], label=sheet, color=color, s=0.5)

# Оформление графика
plt.xlabel("t (s)")
plt.ylabel("U (mV)")
plt.title("График V(t) для разных давлений P")
plt.legend(title="P, Торр")
plt.tight_layout()
plt.grid(True)

plt.savefig("images/graph_raw.png")

plt.figure(figsize=(8, 6))

coeff_texts = []  # Список для сбора коэффициентов

for sheet, color in zip(sheets, colors):
    df = xls.parse(sheet)
    t = df['t (s)']
    ln_V = np.log(df['V (mV)'])
    
    # Рисуем точки
    plt.plot(t, ln_V, 'o', label=f'{sheet}', color=color, markersize=1)
    
    # Рассчитываем коэффициенты линейной регрессии (МНК)
    slope, intercept, _, _, _ = linregress(t, ln_V)
    
    # Добавляем текст в список для последующего вывода под легендой
    coeff_texts.append(f'{sheet}: y = k={slope:.5f}x + b={intercept:.5f}')

plt.xlabel("t (s)")
plt.ylabel("ln(V)")
plt.title("График ln(V) от t с коэффициентами МНК")
plt.legend(title="P, Торр")

# Размещаем текст под легендой
coeff_text = "\n".join(coeff_texts)
plt.annotate(coeff_text, xy=(0.02, 0.02), xycoords='axes fraction', fontsize=10, verticalalignment='bottom')

plt.tight_layout()
plt.grid(True)

# Сохранение графика
plt.savefig("images/graph_ln.png")
plt.close()


