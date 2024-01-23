import os

# Використовуємо os.cpu_count() для отримання кількості ядер
num_cores = os.cpu_count()

# Виводимо результат
print(f"Кількість ядер на комп'ютері: {num_cores}")

