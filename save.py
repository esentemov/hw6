# Функция позволяет сохранить полученные данные в файл, а также задать название файла


def save_data_file(i):
    print("Хотите сохранить результат? Введите 'Да'")
    save_result = input().title()
    if save_result == 'Да':
        sales_analysis = input("Имя файла, в который сохранить результат\n")
        sales_analysis += ".txt"
        s = open(sales_analysis, 'w')
        s.write(str(i))
        s.close()
        print("Файл '" + sales_analysis + "' успешно сохранен")

