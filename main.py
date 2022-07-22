''' Скрипт который переименовывает изображения в указанной дирректории с заданным корнем и порядковым номером. '''
from os import listdir, rename
from sys import argv

# Параметры котрые мы передаем в программу в качестве аргументов
script, path, dir_name = argv


def get_files_list(path):
    '''
    Данная функция возвращает список файлов в котором содержатся нужные для переименования файлы
    :param path:
    :return: files
    '''
    files = listdir(path)  # получение списка файлов в дирректории путь к которой передан в кач-ве параметра

    # Чистка списка
    for file in files:
        if '.jpg' or '.JPG' or '.png' or '.PNG' or '.JPEG' or '.jpeg' in file:  # отбор файла с нужным расширением
            pass
        else:
            files.remove(file)

    return files


def rename_files(files_list, path):
    '''
    Функия переименовывает файлы которые содержатся в поступающем списке
    :param files_list:
    :param path:
    :return:
    '''
    for file in files_list:
        file_old_name = path + file  # Старое имя файла вместе с путем
        file_name = dir_name + '_' + str(files_list.index(file)) + '.jpg'  # Генерируем новое имя файла
        file_new_name = path + file_name  # Новое имя файла вместе с абсолютным путем

        # Переименование файлов
        rename(file_old_name, file_new_name)


def main():
    files_list = get_files_list(path)
    print(
        "[!] ОБРАТИТЕ ВНИМАНИЕ ЧТО ДЛЯ УСПЕШНОЙ РАБОТЫ СКРИПТА ПУТЬ ДОЛЖЕН ЗАКАНЧИВАТЬСЯ СЛЕШЕМ\n Желаете продолжить? "
        "(y/n)"
    )

    state = input().lower()
    if state == 'y':
        rename_files(files_list, path)
    elif state == 'n':
        print("Ну как хочешь...")
        quit()
    else:
        print("Не понимаю о чем вы говорите. Бай!")
        quit()
    print('[Файлы в указанной дирректории переименованы.]')


if __name__ == "__main__":
    main()
