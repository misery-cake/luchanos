"""
Задача 3.2
3.2.1.
Написать декоратор, который внутри себя выполнял бы функцию и возвращал бы результат её работы в случае успешного
выполнения. В случае возникновения ошибки во время выполнения функции нужно сделать так, чтобы выполнение функции было
повторено ещё раз с теми же самыми аргументами, но не более 10 раз. Если после последней попытки функцию так и не
удастся выполнить успешно, то бросать исключение.
"""


def repeater(func):
    def inner(*args, **kwargs):
        max_attempts = 3
        attempts_left = max_attempts
        while attempts_left > 0:
            try:
                return func(*args, **kwargs)
            except Exception as err:
                attempts_left -= 1
                print('Ошибка:', err, 'попыток осталось:', attempts_left)
                if attempts_left == 0:
                    raise
    return inner


@repeater
def foo():
    raise ValueError('Какая-то ошибка')


"""
3.2.2.
Параметризовать декоратор таким образом, чтобы количество попыток выполнения функции можно было задавать
как параметр во время декорирования.
"""


def parametrized_repeater(max_attempts=3):
    def decorator(func):
        def inner(*args, **kwargs):
            attempts_left = max_attempts
            while attempts_left > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    attempts_left -= 1
                    print('Ошибка:', err, 'попыток осталось:', attempts_left)
                    if attempts_left == 0:
                        raise
        return inner
    return decorator


@parametrized_repeater
def bar():
    raise ValueError('Без параметра')


@parametrized_repeater(max_attempts=1)
def fizz():
    raise ValueError('С параметром')


fizz()
