import numpy as np

import scipy.integrate as spi


def f(x):
    return x ** 2


a = 0
b = 2

n = 10000

x_random = np.random.uniform(a, b, n)
y_random = f(x_random)

# Обчислення методом Монте-Карло
integral_monte_carlo = (b - a) * np.mean(y_random)

# Обчислення інтеграла за допомогою функції quad
result, error = spi.quad(f, a, b)

print(f"Інтеграл (Метод Монте-Карло): {integral_monte_carlo}")
print(f"Інтеграл (Функція quad): {result}")
