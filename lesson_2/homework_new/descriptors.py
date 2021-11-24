class Port:
    def __set__(self, instance, value):
        if not 0 <= value < 65536:
            exit(1)
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

