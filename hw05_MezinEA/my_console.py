import sys
def help():
    print("""
    help - вывод этой справки
    ping - проверка работы программы
    """)

def ping():
    print('pong')

do = {
    'help' : help,
    'ping' : ping
}

if 'name' == '__main__':
    command = sys.argv[1]
    if command in do:
        do[command]()
    else:
        help()
        