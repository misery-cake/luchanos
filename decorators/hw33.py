"""
3.3.1
Написать кэширующий декоратор. Суть в том, что если декорируемая функция будет запущена с теми параметрами с которыми
она уже запускалась - брать результат из кэша и не производить повторное выполнение функции.
"""
from collections import namedtuple
from datetime import datetime, timedelta
from time import sleep


def memoize(func):
    """Не рабоает для изменяемых позиционных и ключей именованных аргументов."""
    cache = {}

    def inner(*args, **kwargs):
        cache_key = args + tuple(sorted(kwargs.items()))
        if cache_key not in cache:
            cache[cache_key] = func(*args, **kwargs)
        return cache[cache_key]
    return inner


"""
3.3.2
Сделать так, чтобы информация в кэше была актуальной не более 10 секунд. Предусмотреть механизм автоматической
очистки кэша в процессе выполнения функций.
"""

CacheElement = namedtuple('CacheElement', 'value timestamp')


def expiring_memoize(func):
    """Не рабоает для изменяемых позиционных и ключей именованных аргументов."""
    cache_ttl_seconds = 2
    cache = {}

    def _clear_outdated():
        """Очищает кэш от старых данных."""
        keys_to_delete = []
        for key, value in cache.items():
            diff = datetime.now() - value.timestamp
            if diff > timedelta(seconds=cache_ttl_seconds):
                keys_to_delete.append(key)
        for key in keys_to_delete:
            cache.pop(key)

    def inner(*args, **kwargs):
        _clear_outdated()
        cache_key = args + tuple(sorted(kwargs.items()))
        if cache_key not in cache:
            cache[cache_key] = CacheElement(
                value=func(*args, **kwargs),
                timestamp=datetime.now(),
            )
        return cache[cache_key].value

    return inner


some_data = iter(['a', 'b'])


@expiring_memoize
def foo():
    return next(some_data)


# первый раз попали в кэш
assert foo() == 'a'
sleep(1)
# в кэше актуальное значение
assert foo() == 'a'
sleep(2)
# кэш очистился и там теперь новое значение
assert foo() == 'b'
assert foo() == 'b'


"""
3.3.3
Параметризовать время кэширования в декораторе.
"""


def parametrized_expiring_memoize(cache_ttl_seconds=10):
    def decorator(func):
        """Не работает для изменяемых позиционных и ключей именованных аргументов."""
        cache = {}

        def _clear_outdated():
            """Очищает кэш от старых данных."""
            keys_to_delete = []
            for key, value in cache.items():
                diff = datetime.now() - value.timestamp
                if diff > timedelta(seconds=cache_ttl_seconds):
                    keys_to_delete.append(key)
            for key in keys_to_delete:
                cache.pop(key)

        def inner(*args, **kwargs):
            _clear_outdated()
            cache_key = args + tuple(sorted(kwargs.items()))
            if cache_key not in cache:
                cache[cache_key] = CacheElement(
                    value=func(*args, **kwargs),
                    timestamp=datetime.now(),
                )
            return cache[cache_key].value
        return inner
    return decorator


some_data = iter(['a', 'b'])


@parametrized_expiring_memoize(5)
def bar():
    return next(some_data)


# первый раз попали в кэш
assert bar() == 'a'
sleep(1)
# в кэше актуальное значение
assert bar() == 'a'
sleep(5)
# кэш очистился и там теперь новое значение
assert bar() == 'b'
assert bar() == 'b'
