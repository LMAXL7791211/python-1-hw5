
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
    print("Папки текущей директории:", os.listdir())



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file():
    print('os.getcwd() = ', os.getcwd())

import os
copy_file()