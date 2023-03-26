class AutoGetSet(type):
    def __new__(cls, name, bases, dct):
        attributes = dct.get('_attributes', [])
        for attr in attributes:
            getter = lambda self, attr=attr: getattr(self, '_' + attr)
            setter = lambda self, value, attr=attr: setattr(self, '_' + attr, value)
            dct['get_' + attr] = getter
            dct['set_' + attr] = setter
            dct[attr] = property(getter, setter)
        return super().__new__(cls, name, bases, dct)