
import csv

RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
BLUE = '\u001b[44m'

with open('books.csv', 'r', encoding='cp1251') as f:

    table = csv.reader(f, delimiter=';')
    older_than_12 = 0
    younger_than_12 = 0
    for row in table:
        if row[5].isdigit():
            if int(row[5]) == 12:
                older_than_12 += 1
            else:
                younger_than_12 += 1


# Инициализация массива
plot = [[0 for col in range(8)] for row in range(21)]

older_percent = round(older_than_12 / (older_than_12 + younger_than_12) * 100)
younger_percent = round(younger_than_12 / (older_than_12 + younger_than_12) * 100)

for i in range(21):
    plot[i][0] = f'{100-i*5}%'

for i in range(21):
    for j in range(8):
        if older_percent > 100-i*5:
            plot[i][2] = 1
            plot[i][3] = 1
        if younger_percent > 100-i*5:
            plot[i][5] = 2
            plot[i][6] = 2

for i in range(21):
    line = ''
    for j in range(8):
        if j == 0:
            line += f'{WHITE}{plot[i][0]}\t {END}'
        elif plot[i][j] == 0:
            line += f'{WHITE}   {END}'
        elif plot[i][j] == 1:
            line += f'{RED}   {END}'
        elif plot[i][j] == 2:
            line += f'{BLUE}   {END}'
    print(line)

print(f'\n{RED} Для 12 лет - {older_than_12} книг\t{END}\n{BLUE} Для остальных - {younger_than_12} книг\t{END}')








