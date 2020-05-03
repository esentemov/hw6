# ДЗ 1. Cделать программу  финансового учета, которая на вход принимает файл, который ей указали,
# в котором цифры должны быть расположены построчно. Программа выдает простейшие статистики,
# такие как суммы и среднее, которые она записывает в файл вывода, которые она сама генерирует

import time
from save import save_data_file as saveme

print("Здравствуйте! Спасибо, что приобрели 'ФинУчет1999'.\n"
      "Программа поможет вам проанализировать ваши продажи.\n"
      "Вы можете загрузить файл для дальнейшей обработки.")
name_of_file = input("\nВведите имя файла, который вы хотите загрузить: ")
name_of_file += ".txt"

with open(name_of_file) as file:
    lines = file.read().splitlines()
    lines = [int(line) for line in lines]

    # Присваиваем элементам в списке тип integer

    print("Подождите, файл загружается...")
    time.sleep(1)

    # Показываем, что программа загружает файл (1 секунду)

    def analysis():
        day = input("Файл с данными о продажах успешно загружен. Какие данные вывести на экран?\n"
                    "1 - показать продажи в исходном виде\n"
                    "2 - показать продажи в строку\n"
                    "3 - сумму продаж\n"
                    "4 - средний чек\n"
                    "5 - количество продаж\n")
        for line in lines:
            if day == '1':
                print(line)
        if day == '2':
            print(lines)
            saveme(lines)
        if day == '3':
            sum_of_sales = sum(lines)
            print("Сумма продаж:", sum_of_sales, "руб.")
            saveme(sum_of_sales)
        if day == '4':
            average_of_sales = round(sum(lines) / len(lines), 3)
            print("Средний чек:", average_of_sales, "руб.")
            saveme(average_of_sales)
        if day == '5':
            qty = len(lines)
            print("Количество продаж:", qty)
            saveme(qty)

    analysis()

    while True:
        new_try = input("Хотите получить новые данные? Введите 'Да'\n"
                        "Специально для вас есть уникальное предложение ;) Введите 'секрет'\n").title()
        if new_try == "Да":
            analysis()
        elif new_try == "Секрет":
            forecast = input("Хотите получить прогноз продаж на месяц? Введите 'Да'\n").title()
            if forecast == "Да":
                print("Обработка платежа...")
                time.sleep(2)
                print("С вашей банковской карты списано 100$")
                print("Считаем прогноз...")
                time.sleep(3)
                if name_of_file == "monday.txt" or "tuesday.txt" or "wednesday.txt" or "thursday.txt" or "friday.txt":
                    print("По нашему точному прогнозу, продажи за месяц составят",
                          (sum(lines) * 22 + sum(lines) * 2 * 9), "руб.")

                    # считаем, что в выходные продаж больше в 2 раза, поэтому продажи за 9 дней выходных умножаем на 2

                elif name_of_file == "saturday.txt" or "sunday.txt":
                    print("По нашему точному прогнозу, продажи в месяц составят",
                          (sum(lines) * 22 * 0.5 + sum(lines) * 9), "руб.")
            else:
                print("Очень жаль :(")
        else:
            print("Хорошего дня!")
            exit()
