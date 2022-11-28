"""
Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен только
последний октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.
"""

from ipaddress import ip_address
from task_1 import host_ping


def host_range_ping():
    count_ip = None
    ip = None
    while True:
        start_ip = input('Введите начальный IP-адрес: ')
        try:
            ip = ip_address(start_ip)
        except ValueError:
            print('Вы ввели не IP-адрес')
            break
        count_ip = int(input('Введите количество проверяемых адресов: '))
        last_octet = int(ip) % 256
        if last_octet + count_ip > 256:
            print(f'Максимальное число IP-адресов для проверки: {256 - last_octet}, включая введенный адрес')
        else:
            break
    ip_list = []
    for i in range(count_ip):
        ip_list.append(ip + i)
    return host_ping(ip_list)


def main():
    host_range_ping()


if __name__ == '__main__':
    main()
