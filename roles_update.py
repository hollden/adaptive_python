#!/bin/python
# -*- coding: UTF-8 -*-

# Скрипт, применяющий выдачу грантов для требуемой роли на все бд постргеса
# Запуск: python roles_update.py path_to_script database1,database2,database3....databaseN
# path_to_script - скрипт, выдающий гранты в самой бд
# databaseN - применение скрипта к базам по списку через запятую (не является обязательным)

# version 0.3
import sys
import os


def main():
    if len(sys.argv) > 1:
        path_to_script = sys.argv[1]
    else:
        print('Enter path to script')
        sys.exit()

    if len(sys.argv) == 3:
        list_of_databases = sys.argv[2].split(',')
    else:
        command = 'psql -X -A -t -1 -c "SELECT datname FROM pg_database WHERE NOT datistemplate;"'
        list_of_databases = [s for s in os.popen(command).read().split('\n') if s !='']

    print('List of databases:')
    print(' '.join(list_of_databases))

    not_include_databases = ['template0', 'template1']

    for database in list_of_databases:
        if database.strip() not in not_include_databases:
            print('\n\n')
            # проверяем наличие dblink
            command = 'psql -d {} -X -A -t -1 -c "SELECT EXISTS(SELECT extname FROM pg_extension WHERE extname = \'dblink\');"'.format(database)
            if os.popen(command).read().strip() == 'f':
                command = 'psql -d {} -c "create extension dblink;"'.format(database)
                os.system(command)
            # выдаем необходимые гранты
            command = 'psql -d {} -f {}'.format(database, path_to_script)
            print(command)
            os.system(command)


if __name__ == '__main__':
    main()