from re import X
import numpy

# Constants

T_f = 10
v_f = 10**6

"""def calc_eigenvalue(m, t):

    #Calculates m-th eigenvalue in terms of gamma = even eigenvalue

    m += 2
    if m % 2:
        return (m**4 * t**2)/(1 + m**4 * t**2)
    else:
        return 1
"""
def calc_eigenvalue(m, t):

    m += 2
    if m % 2:
        return t**2
    else:
        return 1

def equal(x, y):
    """
    Checks if the eigenvalues are of the same order
    """
    if x < y:
        x, y = y, x
    return x / y < 1.02

"""def gen_eigenvalues(t):

    #Generates a list of eigenvalues. The list ends then eigenvalues become equal (see the definition in corresponding function)
    
    eigenvalues = [calc_eigenvalue(0, t)]
    i = 1
    while not equal(eigenvalues[-1], calc_eigenvalue(i, t)):
        eigenvalues.append(calc_eigenvalue(i, t))
        i += 1
    return eigenvalues"""



def gen_eigenvalues_n(t, n):
    
    eigenvalues = [calc_eigenvalue(0, t)]
    i = 1
    while i<=2*n:
        eigenvalues.append(calc_eigenvalue(i, t))
        eigenvalues.append(calc_eigenvalue(i + 1, t))
        i += 2
    return eigenvalues

def gen_eigenvalues(t):
    n = 1
    return gen_eigenvalues_n(t, n)
    
def save_results(filename, xaxis, yaxis, xdata, ydata):
    """
    Saves results of calculations in file which is used for plotting
    """
    # To Do: add more sections of data to build many curves in one field

    with open(filename, 'w') as f:
        f.write(xaxis+" "+yaxis+"\n")
        for i in range(len(xdata)):
            f.write(str(xdata[i])+" "+str(ydata[i])+"\n")
        f.close()

def calc_sigma(t, s, eigenvalues, m):
    """
    Counts sigma 
    """
    if m == len(eigenvalues) - 1:
        #return eigenvalues[m] + 0.5*(numpy.sqrt(1+4*s) - 1)
        return eigenvalues[m] + s
    else:
        return eigenvalues[m] + s/calc_sigma(t, s, eigenvalues, m + 1)

def Sum(t, s_0):
    n = 1
    sum0 = 0
    s = s_0*n**2
    while (calc_sigma(t, s, gen_eigenvalues(t), 0)/s / (sum0+1e-10) > 10**(-3)):
        sum0+=calc_sigma(t, s, gen_eigenvalues(t), 0)/s
        n += 1
        s = s_0*n**2
        print(s, calc_sigma(t, s, gen_eigenvalues(t), 0), calc_sigma(t, s, gen_eigenvalues(t), 0)/s)
    return sum0* s_0 * 6/ numpy.pi**2

'''
xdata = numpy.logspace(start = -8, stop = -3, num = 100)
ydata = []
for i in range(len(xdata)):
    ydata.append(Sum(0.001, xdata[i]))

save_results("0001LineK.txt", "nu*k**2", "sigma", xdata, ydata)

'''

xdata = numpy.logspace(start = -3, stop = -0, num = 100)
ydata = []
for i in range(len(xdata)):
    ydata.append(Sum(xdata[i], 1e-3))

save_results("-3.txt", "nu*k**2", "sigma", xdata, ydata)


'''
xdata = numpy.logspace(start = -8, stop = 1, num = 100)
ydata = []
for i in range(len(xdata)):
    t = 1
    s = xdata[i]
    k = 0.5*(numpy.sqrt(1+4*s) - 1)/s
    ydata.append(k*calc_sigma(t, s, gen_eigenvalues(t), 0))

save_results("1.txt", "nu*k**2", "sigma", xdata, ydata)
'''

"""xdata = numpy.logspace(start = -3, stop = 0, num = 100)
ydata = []
for i in range(len(xdata)):
    ydata.append(calc_eigenvalue(0, xdata[i]))

save_results("2.txt", "nu*k**2", "sigma", xdata, ydata)"""
