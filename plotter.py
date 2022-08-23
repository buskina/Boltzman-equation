import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)
import numpy as np


def readfile(filename):
    x = []
    y = []
    f = open(filename,'r')
    lines = f.readlines()
    f.close()
    
    for line in lines[1:]:
        x_and_y = line.split()
        #print(x_and_y)
        x.append(float(x_and_y[0]))
        y.append(float(x_and_y[1]))
    
    return np.array(x), np.array(y)

########################################################################
    
#Plotting params

plt.rcParams['text.usetex'] = True
plt.rcParams['figure.figsize'] = (8,6)
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = '18'
plt.rcParams['figure.autolayout'] = True
plt.rcParams["legend.frameon"] = False
plt.rcParams["errorbar.capsize"]=5

########################################################################


#Eigenvalues as a function of Temperature

x, y = readfile('3.txt')
#print(x)
#print(y)

# Диапазон осей
#X_LIM_BOTTOM = 0.003
#Y_LIM_BOTTOM = 0.9

#X_LIM_UP = 0.0036
#Y_LIM_UP = 1.2

# Данные

#x1 = [0.003409362,0.003298262,0.003193052,0.003094059]
#y1 = [1.125,1.039,0.985,0.922]

# Значения погрешностей
#yerr = [0.05, 0.03, 0.02, 0.01]
#xerr = 0.00005

fig, ax = plt.subplots()



# Диапазоны осей
#ax.set_xlim(X_LIM_BOTTOM, X_LIM_UP)
#ax.set_ylim(Y_LIM_BOTTOM, Y_LIM_UP)

ax.set_xscale('log')
ax.set_yscale('log')

# Шаг сетки для главных делений
#ax.xaxis.set_major_locator(MultipleLocator(0.00005))
#ax.yaxis.set_major_locator(MultipleLocator(0.05))

# Количество промежутков между главными делениями
#ax.xaxis.set_minor_locator(AutoMinorLocator(5))
#ax.yaxis.set_minor_locator(AutoMinorLocator(5))

# Сетка для главных и дополнительных делений
ax.grid(which='major', color='#CCCCCC', linestyle='--')
ax.grid(which='minor', color='#CCCCCC', linestyle=':')

# Отображение крестов погрешности
#ax.errorbar(x1, y1, yerr=yerr, xerr=xerr, fmt = '.k', ecolor='#666666', capthick=1)

# Подписи осей
plt.xlabel(r'Temperature of the system $\ln T/T_F$')
plt.ylabel(r'Eigenvalues $\gamma_m$, arbitrary scale')

# Название графика
#plt.title('График 2. Зависимость |μ|(1/T)')


#h1 = np.arange(X_LIM_BOTTOM, X_LIM_UP, (X_LIM_UP-X_LIM_BOTTOM)/100)
#p1, cov1= np.polyfit(x, y,  rcond=None, full=False, w=None, cov=True)
#plt.plot(h1, h1*p1[0]+p1[1], color = '#a0a0a0')
plt.plot(x, y, linewidth = 3)


#print('k1 =', p1[0], ' b1 =', p1[1])
#print(cov1)
#print('σ(k1) =', cov1[0][0]**0.5, ' σ(b1) =',  cov1[1][1]**0.5)

plt.show()
plt.savefig('eigenvalues.pdf')