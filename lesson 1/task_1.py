"""
Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или
ip-адресом. В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции
ip_address().
"""
import platform
from ipaddress import ip_address
from subprocess import Popen, PIPE


def host_ping(ip_list):
    res = {
        'Доступные узлы': '',
        'Недоступные узлы': ''
    }
    for ip in ip_list:
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        try:
            ip = ip_address(ip)
        except ValueError:
            pass
        command = ['ping', param, '1', str(ip)]
        process = Popen(command, shell=False, stdout=PIPE)
        process.wait()
        if process.returncode == 0:
            res['Доступные узлы'] += f'{str(ip)}\n'
            print(f'Узел {ip} доступен')
        else:
            res['Недоступные узлы'] += f'{str(ip)}\n'
            print(f'Узел {ip} не доступен')
    return res


def main():
    ip_list = [
        '12.111.33.22',
        'ya.ru',
        'mail.ru',
        '192.168.1.1'
    ]
    host_ping(ip_list)


if __name__ == '__main__':
    main()
