from math import sqrt
from scipy.stats import chi2


with open('r3z2.csv') as file:
    numbers = [float(x) for x in file.readlines()[1:]]
    N = len(numbers)    #размер выборки
    Q = 0.99    #коэффициент надежности
    alpha = 1 - Q       #вероятность ошибки
    X = round(sum(numbers) / len(numbers), 2)     #среднее по выборке(практическое)
    dysp = sum((x - X)**2 for x in numbers) / N      #дисперсия по выборке
    S = sqrt(dysp)      # отклонение фактическое
    Xp = chi2.ppf(1 - alpha, df=N-1)    # квантиль порядка Alpha распределения хи-квадрат с (n - 1) степенью свободы
    X1_p = chi2.ppf(alpha, df=N-1)      # квантиль порядка 1 - Alpha распределения хи-квадрат с (n - 1) степенью свободы
    low = (N/Xp)*dysp   # нижняя 1-alpha доверительная граница
    high = (N/X1_p)*dysp    # верхняя 1-alpha доверительная граница
    print(f"Фактическая дисперсия: {round(dysp, 4)}\n"
          f"Нижняя {1 - alpha}-доверительная граница для dysp**2: {round(low, 4)}\n"
          f"Верхняя {1 - alpha}-доверительная граница для dysp**2: {round(high, 4)}")
    print(f"Вероятность, что дисперсия по всей совокупности будет в интервале "
          f"от {round(low, 4)} до {round(high, 4)} равна {Q}")