import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error  # mse
from sklearn.metrics import r2_score  # r²
from scipy import stats # calcular zsocre dos dados


x = np.array([0, 3, -1, 4, 3, 5, 2, 10, 2, 4])
y = np.array([0.2, 0.8, 2.4, 6.5, 7.1, 7.5, 7.7, 8.1, 8.9, 10.2])

def doPrevDate():
    # A)
    F = np.polyfit(x, y, 6)
    yy = np.polyval(F, x)

    plt.plot(x, y, '*', label='Real')
    plt.plot(x, yy, 'g--', label='Predição')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('REGRESSÃO')
    plt.show()

    # B)
    r2 = r2_score(y, yy)  # calculo do R²
    print(r2)

    mse = mean_squared_error(y, yy)  # calculo do erro quadratico médio
    print(mse)


doPrevDate()

# C)
x =  stats.zscore(x)
y = stats.zscore(y)

print(x)
print(y)

doPrevDate()

