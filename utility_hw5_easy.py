
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def make_dir_1_dir_9():
    import os
    for i in range(1,10):
        dir_i = ('dir_{}'.format(i))
        if not os.path.exists(dir_i):
            os.mkdir(dir_i)
            print(dir_i)
        else:
            print('{} exists'.format(dir_i))

def rem_dir_1_dir_9():
    import os
    for i in range(1,10):
        dir_i = ('dir_{}'.format(i))
        if os.path.exists(dir_i):
            os.rmdir(dir_i)
            print("{} is removed.".format(dir_i))
        else:
            print('{} not exists'.format(dir_i))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir():
    import os
    print("Папки текущей директории:")
    for i in os.listdir():
        if os.path.isdir(i):
            print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file():
    import shutil
    import sys
    print('исходный  = ', sys.argv[0])
    shutil.copy(sys.argv[0], sys.argv[0] + '.backup')

# утилиты для ДЗ нормал:
def cd(dir):
    import os
    os.chdir(dir)
    print(f'Успешно перешёл в {dir}')

def deld(dir):
    import os
    import shutil
    shutil.rmtree(dir)
    print(f'Успешно удалена папка {dir} со всем содержимым')

def crd(dir):
    import os
    os.mkdir(dir)
    print(f'Успешно создана папка {dir}')

    pass

if __name__ == "__main__":

    copy_file()
