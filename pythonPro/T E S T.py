class TypeCheckedMeta(type):
    def __new__(cls, name, bases, class_dict):
        cls_obj = super().__new__(cls, name, bases, class_dict)
        cls_obj._type_annotations = class_dict.get('__annotations__', {})
        return cls_obj

    def __call__(cls, *args, **kwargs):
        # Создаем экземпляр класса
        instance = super().__call__(*args, **kwargs)

        # Переопределяем метод __setattr__ для экземпляра
        def setattr_check(self, key, value):
            if key in cls._type_annotations:
                expected_type = cls._type_annotations[key]
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Для атрибута '{key}' очікується тип '{expected_type.__name__}', але отримано '{type(value).__name__}'.")
            super(cls, self).__setattr__(key, value)

        # Присваиваем новый метод __setattr__ экземпляру
        instance.__setattr__ = setattr_check.__get__(instance)
        return instance


# Тестовый класс
class Person(metaclass=TypeCheckedMeta):
    name: str = ""
    age: int = 0


class TypeCheckedMeta(type):
    def __new__(cls, name, bases, class_dict):
        cls_obj = super().__new__(cls, name, bases, class_dict)
        cls_obj._type_annotations = class_dict.get('__annotations__', {})
        return cls_obj

    def __call__(cls, *args, **kwargs):
        # Создаем экземпляр класса
        instance = super().__call__(*args, **kwargs)

        # Переопределяем метод __setattr__ для экземпляра
        def setattr_check(self, key, value):
            if key in cls._type_annotations:
                expected_type = cls._type_annotations[key]
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Для атрибута '{key}' очікується тип '{expected_type.__name__}', але отримано '{type(value).__name__}'.")
            super(cls, self).__setattr__(key, value)

        # Присваиваем новый метод __setattr__ экземпляру
        instance.__setattr__ = setattr_check.__get__(instance)
        return instance


class Person(metaclass=TypeCheckedMeta):
    name: str = ""
    age: int = 0


p = Person()
p.name = "John"  # Все добре
p.age = "30"  # Викличе помилку, очікується int

