import numpy as np
from scipy.integrate import odeint  # библиотека для решения обыкновенных дифференциальных уравнений
import matplotlib.pyplot as plt

# Популяция людей, N.
N = 1000

# Количество инфицированных и выздоровевших (имеющих иммунитет), I0 и R0 соотвествтенно.
I0, R0 = 1, 0

# Все остальные, S0, те, кто не заразился, но может быть заражен.
S0 = N - I0 - R0

# beta - скорость заражения, gamma - скорость выздоровления, (в виду 1/дни).
beta, gamma = 0.2, 1. / 10

# Сетка с временными отрезками (в днях)
t = np.linspace(0, 160, 160)

# SIR модель в виде дифуров.
def deriv(y, t, N, beta, gamma) :
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt


# Векторы изначальных условий
y0 = S0, I0, R0
# Интегрируем уравнения модели SIR по времени, t.
ret = odeint(deriv, y0, t, args = (N, beta, gamma))
S, I, R = ret.T

# Поместим полученные данные на три разные кривые, где синим будет - S(t), красным - I(t) и зеленым -  R(t)
fig = plt.figure(facecolor = 'w')

ax = fig.add_subplot(111, facecolor = '#dddddd', axisbelow = True)
ax.plot(t, S / 1000, 'b', alpha = 0.5, lw = 2, label = 'Есть подозрения')
ax.plot(t, I / 1000, 'r', alpha = 0.5, lw = 2, label = 'Заражены')
ax.plot(t, R / 1000, 'g', alpha = 0.5, lw = 2, label = 'Выздоровели')
ax.set_xlabel('Время / дни')
ax.set_ylabel('Количество (1000-и)')
ax.set_ylim(0, 1.2)
ax.yaxis.set_tick_params(length = 0)
ax.xaxis.set_tick_params(length = 0)
ax.grid(b = True, which = 'major', c = 'w', lw = 2, ls = '-')

legend = ax.legend()
legend.get_frame().set_alpha(0.5)

for spine in ('top', 'right', 'bottom', 'left') :
    ax.spines[spine].set_visible(False)

plt.show()
