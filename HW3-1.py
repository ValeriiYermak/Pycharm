"""Напишіть програму обробки папки "Хлам", яка сортує файли у вказаній папці за 
розширеннями з використанням кількох потоків. Пришвидшіть обробку великих 
каталогів з великою кількістю вкладених папок та файлів за рахунок паралельного
виконання обходу всіх папок в окремих потоках. Найбільш витратним за часом буде 
перенесення файлу та отримання списку файлів у папці (ітерація по вмісту 
каталогу). Щоб прискорити перенесення файлів, його можна виконувати в окремому 
потоці чи пулі потоків. Це тим зручніше, що результат цієї операції ви в додатку 
не обробляєте та можна не збирати жодних результатів. Щоб прискорити обхід вмісту 
каталогу з кількома рівнями вкладеності, ви можете обробку кожного підкаталогу 
виконувати в окремому потоці або передавати обробку в пул потоків."""

import argparse
from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging

"""
py main.py --source -s picture
py main.py --output -o dist
"""

parser = argparse.ArgumentParser(description='App for sorting folders')
parser.add_argument('-s', '--source', required=True)  # option that takes a value
parser.add_argument('-o', '--output',default='dist')  # on/off flag
args = vars(parser.parse_args())
source = args.get('source')
output = args.get('output')

folders = []

def grabs_folder(path: Path):
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folder(el)

def sort_file(path: Path):
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix
            new_path = output_folder / ext
            try:
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(el, new_path / el.name)
            except OSError as e:
                logging.error(e)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    base_folder = Path(source)
    output_folder = Path(output)

    folders.append(base_folder)
    grabs_folder(base_folder)
    print(folders)
    threads = []
    for folder in folders:
        th = Thread(target=sort_file, args=(folder,))
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    print('You can delete your starter folders')
