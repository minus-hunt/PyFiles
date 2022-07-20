import os
from data import EXT, DIR_NAME, DIR_PATH


def get_files_list(path):
    # Данная функция возвращает список файлов в котором содержатся нужные для переименования файлы
    files = os.listdir(path)  # список файлов в текущей дирректории

    # Чистка списка
    for file in files:
        if EXT in file:
            pass
        else:
            files.remove(file)

    return files


def rename_files(files_list, path):
    for file in files_list:
        file_old_name = path + file  # Старое имя файла вместе с путем
        file_name = DIR_NAME + '_' + str(files_list.index(file)) + EXT  # Получаем новое имя файла
        file_new_name = path + file_name  # Новое имя файла вместе с абсолютным путем

        os.rename(file_old_name, file_new_name)


def main():
    files_list = get_files_list(DIR_PATH)
    print("[!] ОБРАТИТЕ ВНИМАНИЕ ЧТО ДЛЯ УСПЕШНОЙ РАБОТЫ СКРИПТА ПУТЬ ДОЛЖЕН ЗАКАНЧИВАТЬСЯ СЛЕШЕМ\n Желаете продолжить? (y/n)")
    state = input()

    if state == 'y':
        rename_files(files_list, DIR_PATH)
    elif state == 'n':
        quit()
    else:
        print("Не понимаю о чем вы говорите")


if __name__ == "__main__":
    main()