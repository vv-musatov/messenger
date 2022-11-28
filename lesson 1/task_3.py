"""
Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. Но в данном случае
результат должен быть итоговым по всем ip-адресам, представленным в табличном формате (использовать модуль tabulate).
"""

from tabulate import tabulate
from task_2 import host_range_ping


def host_range_ping_tab():
    res = host_range_ping()
    print(tabulate([res], headers='keys', tablefmt='grid', stralign='center'))


def main():
    host_range_ping_tab()


if __name__ == '__main__':
    main()
