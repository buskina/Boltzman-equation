from re import X
import numpy

# Constants

T_f = 10
v_f = 10**6

def calc_eigenvalue(m, t):
    """
    Calculates m-th eigenvalue in terms of gamma = even eigenvalue
    """
    m += 2
    if m % 2:
        return (m**4 * t**2)/(1 + m**4 * t**2)
    else:
        return 1

def equal(x, y):
    """
    Checks if the eigenvalues are of the same order
    """
    if x < y:
        x, y = y, x
    return x / y < 10

def gen_eigenvalues(t):
    """
    Generates a list of eigenvalues. The list ends then eigenvalues become equal (see the definition in corresponding function)
    """
    eigenvalues = [calc_eigenvalue(0, t)]
    i = 1
    while not equal(eigenvalues[-1], calc_eigenvalue(i, t)):
        eigenvalues.append(calc_eigenvalue(i, t))
        i += 1
    return eigenvalues

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
        return eigenvalues[m] + 0.5*(numpy.sqrt(1+4*s)-1)
    else:
        return eigenvalues[m] + s/calc_sigma(t, s, eigenvalues, m + 1)

xdata = numpy.logspace(start = -3, stop = 2, num = 100)
ydata = []
for i in range(len(xdata)):
    ydata.append(calc_sigma(1, xdata[i], gen_eigenvalues(1), 0))

save_results("1.txt", "nu*k**2", "sigma", xdata, ydata)
