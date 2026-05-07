class Encapsulation:
    def __init__(self):
        self.__private_variable = 0

    def get_private_variable(self):
        return self.__private_variable

    def set_private_variable(self, value):
        self.__private_variable = value

    def public_method(self):
        self.__private_variable += 1
        print(f"Private variable: {self.__private_variable}")


encapsulation = Encapsulation()
encapsulation.public_method()
print(encapsulation.get_private_variable())
encapsulation.set_private_variable(10)
print(encapsulation.get_private_variable())
```

```python
class Encapsulation:
    def __init__(self):
        self.__private_variable = 0

    def get_private_variable(self):
        return self.__private_variable

    def set_private_variable(self, value):
        self.__private_variable = value

    def public_method(self):
        self.__private_variable += 1
        print(f"Private variable: {self.__private_variable}")


encapsulation = Encapsulation()
encapsulation.public_method()
print(encapsulation.get_private_variable())
encapsulation.set_private_variable(10)
print(encapsulation.get_private_variable())
