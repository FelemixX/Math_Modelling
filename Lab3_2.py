#Рандом по Лапласу и по обратной ему функции
import random
import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt
from scipy.stats import laplace

plt.rcParams.update({'font.size': 16})

def inverse_transform_laplace(b, mu, num_samples):
    u = uniform.rvs(size=num_samples)
    x = mu-b*np.sign(u-0.5)*np.log(1-2*np.abs(u-0.5))
    return x


plt.figure(figsize=(8, 4))
plt.hist(inverse_transform_laplace(1, 0, 5000),bins=100, density=True, label='Обратная функция');
x_n = np.linspace(-10, 10, 100)
plt.plot(x_n, laplace().pdf(x_n), lw=4, label='Распределение по лапласу')
plt.legend()
plt.xlabel('x')
plt.ylabel('Плотность')
