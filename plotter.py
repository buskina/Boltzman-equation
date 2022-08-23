import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import numpy as np


# Диапазон осей
X_LIM_BOTTOM = 0.003
Y_LIM_BOTTOM = 0.9

X_LIM_UP = 0.0036
Y_LIM_UP = 1.2


# Данные
x1 = [0.003409362,0.003298262,0.003193052,0.003094059]
y1 = [1.125,1.039,0.985,0.922]

# Значения погрешностей
yerr = [0.05, 0.03, 0.02, 0.01]
xerr = 0.00005

fig, ax = plt.subplots(figsize=(10, 8))

# Диапазоны осей
ax.set_xlim(X_LIM_BOTTOM, X_LIM_UP)
ax.set_ylim(Y_LIM_BOTTOM, Y_LIM_UP)

# Шаг сетки для главных делений
ax.xaxis.set_major_locator(MultipleLocator(0.00005))
ax.yaxis.set_major_locator(MultipleLocator(0.05))

# Количество промежутков между главными делениями
ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

# Сетка для главных и дополнительных делений
ax.grid(which='major', color='#CCCCCC', linestyle='--')
ax.grid(which='minor', color='#CCCCCC', linestyle=':')

# Отображение крестов погрешности
ax.errorbar(x1, y1, yerr=yerr, xerr=xerr, fmt = '.k', ecolor='#666666', capthick=1)

# Подписи осей
plt.xlabel('1/T, 1/K')
plt.ylabel('|μ|, K/атм')

# Название графика
plt.title('График 2. Зависимость |μ|(1/T)')


h1 = np.arange(X_LIM_BOTTOM, X_LIM_UP, (X_LIM_UP-X_LIM_BOTTOM)/100)
p1, cov1= np.polyfit(x1, y1, 1, rcond=None, full=False, w=None, cov=True)
plt.plot(h1, h1*p1[0]+p1[1], color = '#a0a0a0')
plt.plot(x1, y1, 'o', markersize = 3, color = '#000000')


print('k1 =', p1[0], ' b1 =', p1[1])
#print(cov1)
print('σ(k1) =', cov1[0][0]**0.5, ' σ(b1) =',  cov1[1][1]**0.5)

plt.show()