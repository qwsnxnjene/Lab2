from sympy import symbols, diff, ln, solve


with (open("r3z1.csv") as file):
    numbers = [int(x) for x in file.readlines()[1:]]
    q = symbols('q')    # вводим переменную q
    # функция правдоподобности(произведение вероятностей)
    Lx = ((2*q/3) ** numbers.count(0)) * ((q/3) ** numbers.count(1)) * \
         ((2/3 - 2*q/3) ** numbers.count(2)) * ((1/3 - q/3) ** numbers.count(3))
    # логарифмируем
    lnLx = ln(Lx)
    # находим производную
    d = diff(lnLx)
    # решаем уравнение и выводим ответ
    print(round(*solve(d, q), 4))
