import numpy
import json

# Constants

T_f = 10
v_f = 10^6

def calc_eigenvalue(m, t):
    """
    Calculates m-th eigenvalue in terms of gamma = even eigenvalue
    """
    m += 2
    if m % 2:
        return (m^4 * t^2)/(1 + m^4 * t^2)
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
            f.write(xdata[i]+" "+ydata[i]+"\n")
        f.close()

def count_sigma(t, L, n, eigenvalues, m):
    """
    Counts sigma 
    """
    # To Do: Is it OK to leave this calculations here?

    gamma = t^2
    nu = v_f^2/(4 * gamma)
    k = 2 * numpy.pi/L * n
    sum_pres = 0.5 * (numpy.sqrt(1 + 4 * nu * k^2/gamma) - 1)
    sum_approx = nu * k^2/gamma

    if m == len(eigenvalues) - 1:
        return eigenvalues[m] + sum_approx
    else:
        return eigenvalues[m] + sum_approx/count_sigma(t, L, n, eigenvalues, m + 1)




