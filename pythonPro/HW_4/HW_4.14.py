class TypeCheckedMeta(type):
    def __new__(cls, name, bases, class_dict):
        # Создаем новый класс с использованием метакласса
        cls_obj = super().__new__(cls, name, bases, class_dict)
        # Сохраняем аннотации типов в атрибуте _type_annotations
        cls_obj._type_annotations = class_dict.get('__annotations__', {})
        return cls_obj

    def __call__(cls, *args, **kwargs):
        # Создаем экземпляр класса
        instance = super().__call__(*args, **kwargs)

        # Переопределяем метод __setattr__ для экземпляра
        def setattr_check(self, key, value):
            if key in self.__class__._type_annotations:
                expected_type = self.__class__._type_annotations[key]
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Для атрибута '{key}' очікується тип '{expected_type.__name__}', "
                        f"але отримано '{type(value).__name__}'."
                    )
            super(object, self).__setattr__(key, value)

        # Устанавливаем новый метод __setattr__ экземпляру
        instance.__setattr__ = setattr_check.__get__(instance)
        return instance


# Класс, заданный в условии
class Person(metaclass=TypeCheckedMeta):
    name: str = ""
    age: int = 0


# Пример использования
p = Person()
p.name = "John"  # Все хорошо
try:
    p.age = "30"  # Выдаст ошибку: ожидается int, а не str
except TypeError as e:
    print(e)  # Ожидаемый вывод
