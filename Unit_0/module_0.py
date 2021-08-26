import numpy as np


def game_core_v3(number):
    # Первую попытку делаем посередине, а потом смещаем границы отрезка в зависимости от того,
    # в правой или левой части отрезка оказалось загаданное число
    # Функция принимает загаданное число и возвращает число попыток
    count = 1
    left = min_num
    right = max_num
    predict = (max_num + min_num) // 2
    while number != predict:
        count += 1
        if number > predict:
            left = predict + 1                          # Смещаем левую границу отрезка вправо
            predict = (left + right) // 2               # Предсказываем новое значение
        elif number < predict:
            right = predict - 1                         # Смещаем правую границу отрезка влево
            predict = (left + right) // 2               # Предсказываем новое значение
    return count                                        # Выход из цикла, если угадали


def score_game(game_core):
    # Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
    count_ls = []
    start = np.random.randint(1, 2 ** 11 - 1)           # Генерируем параметр для RANDOM SEED
    np.random.seed(start)                               # Фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим!
    random_array = np.random.randint(1, max_num + 1, size=array_size)
    print(f"Массив загаданных чисел {random_array}")    # Выводим массив загаданных чисел
    for number in random_array:
        count_ls.append(game_core(number))              # Пополняем массив количества попыток для всех чисел
    score = float(np.mean(count_ls))                    # Определяем среднее количество попыток на отгадывание
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


array_size = 1000                               # Размер массива генерируемых чисел
min_num = 1                                     # Минимальное значение генерируемых чисел
max_num = 100                                   # Максимальное значение генерируемых чисел

score_game(game_core_v3)                        # Запускаем процесс генерации и отгадывания чисел
