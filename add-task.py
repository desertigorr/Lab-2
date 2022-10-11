import os
import time

# Пару слов о том, как это было сделано:
# Картинка animation.png преобразована в ASCII-art
# и выведена на экран в определенной последовательности :)

# Инициализация clear-функции
clear = lambda: os.system('cls')


with open('animation.txt') as f:

    lines = f.readlines()

    while True:
        for i in range(5):
            for k in range(16):
                print(lines[i*16 + k], end='')
            time.sleep(0.2)
