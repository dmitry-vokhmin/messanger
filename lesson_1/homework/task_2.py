"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""

from ipaddress import ip_address
from task_1 import host_ping


def host_range_ping(address, address_range):
    host_list = [str(ip_address(address)+end) for end in range(address_range)]
    return host_ping(host_list)


if __name__ == "__main__":
    host_range_ping('127.0.0.1', 10)
