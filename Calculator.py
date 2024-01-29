flag = 0

while True:
    num1 = int(input('Введи первое число: '))
    num2 = int(input('Введи второе число: '))
    operation = input('Напиши, какую операцию вы хотите выполнить. Если не знаешь напиши "Нет": ')

    if operation == 'Нет':  # Инструкция
        print('"+" сумма')
        print('"-" вычетание')
        print('"*" умножение')
        print('"/" самое простое деление')
        print('"//" это целочисленное деление')
        print('"%" это остаток от деления')
        print('"**" это возведение в степень')
    elif operation == '+':  # Суммма
        print(num1 + num2)
        while flag == 0:
            question = input('Хочешь закончить? Если да пиши "Да". Если нет, то пиши "Нет": ')
            if question == 'Да':
                break
            elif question == 'Нет':
                flag += 1
            elif question != 'Да' and question != 'Нет':
                print("Введите занаво")
    elif operation == '-':  # Вычетание
        print(num1 - num2)
        while flag == 0:
            question = input('Хочешь закончить? Если да пиши "Да". Если нет, то пиши "Нет": ')
            if question == 'Да':
                break
            elif question == 'Нет':
                flag += 1
            elif question != 'Да' and question != 'Нет':
                print("Введите занаво")
    elif operation == '*':  # Умножение
        print(num1 * num2)
        while flag == 0:
            question = input('Хочешь закончить? Если да пиши "Да". Если нет, то пиши "Нет": ')
            if question == 'Да':
                break
            elif question == 'Нет':
                flag += 1
            elif question != 'Да' and question != 'Нет':
                print("Введите занаво")
    elif operation == '/':  # Деление
        print(num1 / num2)
        while flag == 0:
            question = input('Хочешь закончить? Если да пиши "Да". Если нет, то пиши "Нет": ')
            if question == 'Да':
                break
            elif question == 'Нет':
                flag += 1
            elif question != 'Да' and question != 'Нет':
                print("Введите занаво")
    elif operation == '//':  # Целочисленное деление
        print(num1 // num2)
        while flag == 0:
            question = input('Хочешь закончить? Если да пиши "Да". Если нет, то пиши "Нет": ')
            if question == 'Да':
                break
            elif question == 'Нет':
                flag += 1
            elif question != 'Да' and question != 'Нет':
                print("Введите занаво")
    elif operation == '%':  # Остаток от деления
        print(num1 % num2)
        while flag == 0:
            question = input('Хочешь закончить? Если да пиши "Да". Если нет, то пиши "Нет": ')
            if question == 'Да':
                break
            elif question == 'Нет':
                flag += 1
            elif question != 'Да' and question != 'Нет':
                print("Введите занаво")
    elif operation == '**':  # Возведение в степень
        print(num1 ** num2)
        while flag == 0:
            question = input('Хочешь закончить? Если да пиши "Да". Если нет, то пиши "Нет": ')
            if question == 'Да':
                break
            elif question == 'Нет':
                flag += 1
            elif question != 'Да' and question != 'Нет':
                print("Введите занаво")
    else:
        print('Неправильное значение. Введите занаво операцию')
