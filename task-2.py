# Task 2 - Endless pattern

# Создание констант
BLACK = '\u001b[40m'
WHITE = '\u001b[47m'
END = '\u001b[0m'


# Инициализация массива
plot = [[0 for col in range(11)] for row in range(5)]


# Создание узора
def draw_pattern(array):
    for i in range(5):
        for j in range(11):
            if i == 0 and j in [0, 1, 9, 10]:
                array[i][j] = 1
            if i == 1 and j in [2, 3, 7, 8]:
                array[i][j] = 1
            if i == 2 and j in [4, 6]:
                array[i][j] = 1
            if i in [3, 4] and j == 5:
                array[i][j] = 1
    return array


# Окрашивание узора
def draw_plot(array_pl, times):
    for i in range(5):
        line = ''
        for j in range(11):
            if j == 0:
                line += WHITE
            if array_pl[i][j] == 0:
                line += '  '
            if array_pl[i][j] == 1:
                line += BLACK + '  ' + WHITE
        line += END
        print(line * times)


# Вывод узора на экран
def create_pattern(times):
    if not times.isdigit():
        print('Необходимо ввести целое число')
        start()
    elif times.isdigit():
        draw_plot(plot, int(times))


# Запуск программы
def start():
    user_input = input('Введите количество повторений узора: ')
    create_pattern(user_input)


draw_pattern(plot)
draw_plot(plot, 1)

start()
