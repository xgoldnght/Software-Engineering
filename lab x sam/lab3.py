class MyClass:
    def __init__(self, value):
        self._value = value
    def set_value(self, value):
        self._value = value
    def get_value(self):
        return self._value
    def del_value(self):
        del self._value
    value = property(get_value, set_value, del_value, 'Свойство value')
obj = MyClass(42)
print(obj.get_value())
obj.set_value(45)
print(obj.get_value())
obj.set_value(100)
print(obj.get_value())
obj.del_value()
print(obj.get_value())