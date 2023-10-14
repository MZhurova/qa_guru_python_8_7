from utils import RESOURCES_PATH, TMP_PATH
from zipfile import ZipFile
import os
import datetime

def test_zipfile():
    if not os.path.exists(TMP_PATH):
        os.mkdir(TMP_PATH)

    with ZipFile(f'{TMP_PATH}/zipfile.zip', 'w') as zf:
        for root, dirs, files in os.walk(RESOURCES_PATH):
            for file in files:
                add_file = os.path.join(root, file)
                file_path = os.path.relpath(add_file, RESOURCES_PATH)
                zf.write(add_file, file_path)

    with ZipFile(f'{TMP_PATH}/zipfile.zip', mode='a') as zf:
        for file in zf.namelist():
            print(file)


    with ZipFile(f'{TMP_PATH}/zipfile.zip') as zf:
        text = zf.read('Hello.txt')
        print(text)

    with ZipFile(f'{TMP_PATH}/zipfile.zip') as zf:
         for file in zf.namelist():
            if file == os.path.basename(os.path.join(RESOURCES_PATH, 'file_example_XLS_10.xls')):
                print(f'Файл {file} в архиве zipfile.zip соответствует файлу из каталога {RESOURCES_PATH}')
            if file == os.path.basename(os.path.join(RESOURCES_PATH, 'file_example_XLSX_50.xlsx')):
                print(f'Файл {file} в архиве zipfile.zip соответствует файлу из каталога {RESOURCES_PATH}')
            if file == os.path.basename(os.path.join(RESOURCES_PATH, 'Hello.txt')):
                print(f'Файл {file} в архиве zipfile.zip соответствует файлу из каталога {RESOURCES_PATH}')
            if file == os.path.basename(os.path.join(RESOURCES_PATH, 'Python Testing with Pytest (Brian Okken).pdf')):
                print(f'Файл {file} в архиве zipfile.zip соответствует файлу из каталога {RESOURCES_PATH}')
