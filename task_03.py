# Задача 4
# Вывести по номеру месяца кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

user_input = input("Введите номер месяца: ")
month = int(user_input)
days={1:31,
2:28,
3:31,
4:30,
5:31,
6:30,
7:31,
8:31,
9:30,
10:31,
11:30,
12:31}

if month in days:
    print('Вы ввели -', month, 'количество дней -', days[month])
else:
    print('Введён неправильный номер месяца')
