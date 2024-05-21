import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return -2 * y + np.sin(t)

def runge_kutta_4th_order(f, t0, y0, t_end, h):
    t_values = np.arange(t0, t_end + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0
    
    for i in range(1, len(t_values)):
        t = t_values[i-1]
        y = y_values[i-1]
        
        k1 = h * f(t, y)
        k2 = h * f(t + 0.5*h, y + 0.5*k1)
        k3 = h * f(t + 0.5*h, y + 0.5*k2)
        k4 = h * f(t + h, y + k3)
        
        y_values[i] = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        
    return t_values, y_values


t0 = 0
y0 = 1
t_end = 10
h = 0.1

t_values, y_values = runge_kutta_4th_order(f, t0, y0, t_end, h)

plt.plot(t_values, y_values, label='Solución numérica (RK4)')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('Solución de la EDO usando el método de Runge-Kutta de cuarto orden')
plt.legend()
plt.grid(True)
plt.show()
