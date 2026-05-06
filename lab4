import os

#путь к папке с данными создается в папке проекта
DATA_DIR = "data"


def ensure_data_dir():
    """создание директории data"""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


#ЗАДАНИЕ 3
def task3():
    print("ЗАДАНИЕ 3")
    ensure_data_dir()

    #пути к файлам
    file_eng = os.path.join(DATA_DIR, "task3_english.txt")
    file_other = os.path.join(DATA_DIR, "task3_other.txt")

    #очистка файлов перед началом для удобства перезапуска
    open(file_eng, 'w').close()
    open(file_other, 'w').close()

    print("Вам необходимо ввести текст 5 раз.")

    # Шаг 4 инструкции: повторение 5 раз
    for i in range(5):
        #вывод собщения
        print("Введите текст:")

        #ввод переменной
        text = input(f"({i + 1}/5) > ")

#проверка и запись в файл

        #проверка состоит ли строка только из латиницы
        if text.isascii() and text.isalpha():
            with open(file_eng, "a", encoding="utf-8") as f:
                f.write(text + "\n")
            print(f"-> Записано в {file_eng}")
        else:
            with open(file_other, "a", encoding="utf-8") as f:
                f.write(text + "\n")
            print(f"-> Записано в {file_other}")


#ЗАДАНИЕ 5
def task5():
    print("\nЗАДАНИЕ 5")
    ensure_data_dir()

    file_path = os.path.join(DATA_DIR, "task5_output.txt")

      #очистка файла
    open(file_path, 'w').close()

#вывод сообщения
    print("Введите текст:")

#запрос количества шагов n
    try:
        n = int(input("Введите количество строк (n): "))
    except ValueError:
        print("Ошибка: нужно ввести целое число.")
        return

#цикл для записи строк
    for i in range(n):
        text_line = input(f"Строка {i + 1}: ")
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(text_line + "\n")

    print(f"Данные успешно записаны в файл {file_path}")


#запуск функций
if __name__ == "__main__":
    #task3()
    #task5()
