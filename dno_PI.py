name_of_file = "pi_million_digits.txt"
print("Пришло время узнать, есть ли ваша дата рождения в трансцендентном  числе  PI")

pi_str = ""
with open(name_of_file) as file:
    lines = file.readlines()
    for line in lines:
        pi_str += line.strip()

birth = input("Введите дату вашего рождения в формате 'ДДММГГГ': ")
if birth in pi_str:
    print("Здорово! Вы в числе Пи! ")
    first_number_in_pi = pi_str.index(str(birth))

    # Функция возвращает номер первого вхождения введенной даты в числе Пи (первого ее символа)

    print("Ваша дата рождения начинается с", first_number_in_pi - 1, "по счету символа после запятой,"
          " а заканчивается", first_number_in_pi + len(birth) - 2, "по счету символом")

    # Указываем -1 и расположение первого символа даты рождения будет отсчитываться от запятой/точки

    print(pi_str)
else:
    print("В числе Пи не рождаются ;(")
