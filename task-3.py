RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'


# Инициализация массива
# Вписываем значения по осям х и у
def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = st * (9 - i)
            if i == 9:
                array_in[i][j] = j
    return array_in

# Наполняем массив значениями (чтобы нарисовать линию)
def array_fill(array_fi, res, st):
    for i in range(9):
        for j in range(10):
            if abs(array_fi[i][0] - result[9-j]) < st:
                for k in range(9):
                    if 8 - k == j:
                        array_fi[i][k + 1] = 1
    return array_fi

# Создаем рисунок esc-символами по заданному массиву
def draw_plot(array_pl):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + str(array_pl[i][j]) + '\t'
            if array_pl[i][j] == 0:
                line += '  '
            if array_pl[i][j] == 1:
                line += RED + '  ' + WHITE
        line += END
        print(line)
    print(f'{WHITE}  0  1 2 3 4 5 6 7 8 9 {END}')



# Создаем пустой массив 10х10
array_plot = [[0 for col in range(10)] for row in range(10)]
# Здесь храним результат (значение х при определенном y)
result = [0 for col in range(10)]
# Заполняем значения y
for i in range(10):
    result[i] = abs(i)

# Вычисляем шаг для оси y
step = round(abs(result[9] - result[0]) / 9, 1)


array_init(array_plot, step)
array_fill(array_plot, result, step)
draw_plot(array_plot)
