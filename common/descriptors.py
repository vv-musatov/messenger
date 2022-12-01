class PortCheck:
    def __set__(self, instance, value):
        if type(value) != int or value < 0:
            raise ValueError(f'Неверный номер порта: {value}')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name
