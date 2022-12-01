import dis


class ServerVerifier(type):
    def __init__(self, clsname, bases, clsdict):
        methods = []
        attributes = []

        for func_el in clsdict:
            try:
                ret = dis.get_instructions(clsdict[func_el])
            except TypeError as err:
                print(err)
            else:
                for i in ret:
                    if i.opname == 'LOAD_GLOBAL' or i.opname == 'LOAD_METHOD':
                        if i.argval not in methods:
                            methods.append(i.argval)
                    elif i.opname == 'LOAD_ATTR':
                        if i.argval not in attributes:
                            attributes.append(i.argval)

        if 'connect' in methods:
            raise ValueError('Метод connect недопустим для серверного сокета')

        if not ('SOCK_STREAM' in methods):
            raise ValueError('Некорректная инициализация сокета')

        super().__init__(clsname, bases, clsdict)


class ClientVerify(type):
    def __init__(self, clsname, bases, clsdict):
        methods = []

        for func in clsdict:
            try:
                ret = dis.get_instructions(clsdict[func])
            except TypeError as err:
                print(err)
            else:
                for i in ret:
                    if i.opname == 'LOAD_GLOBAL':
                        if i.argval not in methods:
                            methods.append(i.argval)
        if 'socket' in methods:
            raise ValueError('Вызов метода socket недопустим')
        if 'accept' in methods:
            raise ValueError('Вызов метода accept недопустим')
        if 'listen' in methods:
            raise ValueError('Вызов метода listen недопустим')

        super().__init__(clsname, bases, clsdict)
