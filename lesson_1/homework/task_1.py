"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping
будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел
должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять
их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес
сетевого узла должен создаваться с помощью функции ip_address().
"""

from ipaddress import ip_address
from subprocess import Popen, PIPE


def host_ping(list_ip_addresses):
    results = {'Узел доступен': '', 'Узел недоступен': ''}
    for address in list_ip_addresses:
        address = ip_address(address)
        proc = Popen(['ping', f'{address}', '-c', '1', "-W", "500"], shell=False, stdout=PIPE)
        code = proc.wait()

        if code == 0:
            response = f'{address} - Узел доступен'
            results['Узел доступен'] += f'{response}\n'
        else:
            response = f'{address} - Узел недоступен'
            results['Узел недоступен'] += f'{response}\n'
        print(response)

    return results


if __name__ == '__main__':
    ip_addresses = ['127.0.0.3', '127.0.0.2', '127.0.0.1']
    host_ping(ip_addresses)
