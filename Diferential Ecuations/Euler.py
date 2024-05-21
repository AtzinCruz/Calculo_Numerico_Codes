import numpy as np
import matplotlib.pyplot as plt

# Define the function f(t, y)
def f(t, y):
    return y - t**2 + 1

# Euler's method
def euler_method(f, t0, y0, t_end, h):
    t_values = np.arange(t0, t_end + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0
    
    for i in range(1, len(t_values)):
        t = t_values[i-1]
        y = y_values[i-1]
        
        y_values[i] = y + h * f(t, y)
        
    return t_values, y_values

def high(a, b, N):
    return (b - a) / N

# Solution parameters
t0 = 0       # Initial time
y0 = 1       # Initial condition
t_end = 50   # End time
h = 0.1      # Integration step size

# Solve the ODE
t_values, y_values = euler_method(f, t0, y0, t_end, h)

# Plot the solution
plt.plot(t_values, y_values, label='Numerical Solution (Euler)')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Solution of the ODE using Euler\'s method')
plt.legend()
plt.grid(True)
plt.show()
