"""Напишіть реалізацію функції factorize, яка приймає список чисел та повертає список чисел,
на які числа з вхідного списку поділяються без залишку.
Реалізуйте синхронну версію та виміряйте час виконання.
Потім покращіть продуктивність вашої функції, реалізувавши використання кількох ядер процесора
для паралельних обчислень і замірьте час виконання знову. Для визначення кількості ядер на
машині використовуйте функцію cpu_count() з пакета multiprocessing
Для перевірки правильності роботи алгоритму самої функції можете скористатися тестом:
def factorize(*number):
    # YOUR CODE HERE
    raise NotImplementedError() # Remove after implementation
a, b, c, d  = factorize(128, 255, 99999, 10651060)
assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553,
760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]"""

import concurrent.futures
import logging
import time
from multiprocessing import Pool, current_process, cpu_count


def factorize(numbers: list) -> list:
    result_list = []
    for number in numbers:
        temp_list = []
        for num in range(1, number + 1):
            if number % num == 0:
                temp_list.append(num)
        result_list.append(temp_list)
    return result_list

def factorize_multy(number: int) -> list:
    result_list = []
    for num in range(1, number + 1):
        if number % num == 0:
            result_list.append(num)
    return result_list


if __name__ == "__main__":
    lst = [10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000, 10000000]
    start_time = time.time()
    a, b, c, d, *_ = factorize(lst)
    end_time = time.time()
    print(f"Sync time is: {end_time - start_time}")


    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
    #              1521580, 2130212, 2662765, 5325530, 10651060]

    print("Success synchron")


    logger = logging.getLogger()
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)
    logger.setLevel(logging.DEBUG)
    count_core = cpu_count()
    start_time_multy = time.time()


    with Pool(processes=count_core) as pool:
        logger.debug(pool.map(factorize_multy, lst))
    end_time_multy = time.time()
    print(f"Multy_pool time is: {end_time_multy - start_time_multy}")
    start_time_multy2 = time.time()


    with concurrent.futures.ProcessPoolExecutor(count_core) as executor:
        executor.map(factorize_multy, lst)
    end_time_multy2 = time.time()
    print(f"Sync time mylty concarent is: {end_time_multy2 - start_time_multy2}")
    