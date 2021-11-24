import dis


class MetaServer(type):
    def __init__(cls, clsname, bases, clsdict):
        methods = set()
        attrs = set()
        for func in clsdict:
            try:
                generator = dis.get_instructions(clsdict[func])
            except TypeError:
                pass
            else:
                for item in generator:
                    if item.opname == 'LOAD_GLOBAL':
                        if item.argval not in methods:
                            methods.add(item.argval)
                    elif item.opname == 'LOAD_ATTR':
                        if item.argval not in attrs:
                            attrs.add(item.argval)

        if 'connect' in methods:
            raise TypeError('Метода connect не должно быть в классе Server')
        if not ('SOCK_STREAM' in attrs and 'AF_INET' in attrs):
            raise TypeError('Не правильное использование сокетов для работы по TCP')

        super().__init__(clsname, bases, clsdict)


class MetaClient(type):
    def __init__(cls, clsname, bases, clsdict):
        methods = set()
        for func in clsdict:
            try:
                generator = dis.get_instructions(clsdict[func])
            except TypeError:
                pass
            else:
                for item in generator:
                    if item.opname == 'LOAD_GLOBAL':
                        if item.argval not in methods:
                            methods.add(item.argval)

        for command in ('accept', 'listen', 'socket'):
            if command in methods:
                raise TypeError(f'В классе не должно быть метода {command}')
        if not ('get_message' in methods or 'send_message' in methods):
            raise TypeError(f'В классе должны быть реализованы методы работы с сокетами')

        super().__init__(clsname, bases, clsdict)
