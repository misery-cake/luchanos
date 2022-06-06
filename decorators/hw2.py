"""
Easy
Реализовать счетчик, который будет увеличиваться каждый раз, когда у нас осуществляется запуск функции суммирования.
"""

ADDER_CALLS_COUNTER = 0


def adder(a, b):
    global ADDER_CALLS_COUNTER
    ADDER_CALLS_COUNTER += 1
    return a + b


_some_sum = adder(0, 1)
assert ADDER_CALLS_COUNTER == 1


"""
Medium
1. Написать ещё несколько произвольных функций (3-4 штуки) и решить задачу со счетчиком аналогично той, котоая была
решена для запуска функции суммирования.
2. Написать функцию, внутри которой у нас будет объявляться наша функция суммирования и возвращаться в качестве
результата работы из объемлющей функции.
3. Попробуйте вызвать написанную функцию и сохраните результат её работы в переменную. Напечатайте результат на экран.
Что наблюдаете?
4. Осуществите вызов функции суммирования из полученной переменной.
"""

DIVIDER_CALLS_COUNTER = 0


def divider(a, b):
    global DIVIDER_CALLS_COUNTER
    DIVIDER_CALLS_COUNTER += 1
    return a / b


MULTIPLIER_CALLS_COUNTER = 0


def multiplier(a, b):
    global MULTIPLIER_CALLS_COUNTER
    MULTIPLIER_CALLS_COUNTER += 1
    return a * b


DIFFERENTIATOR_CALLS_COUNTER = 0


def differentiator(a, b):
    global DIFFERENTIATOR_CALLS_COUNTER
    DIFFERENTIATOR_CALLS_COUNTER += 1
    return a - b


divider(1, 2)
multiplier(1, 2)
differentiator(1, 2)


assert DIVIDER_CALLS_COUNTER == 1
assert MULTIPLIER_CALLS_COUNTER == 1
assert DIFFERENTIATOR_CALLS_COUNTER == 1


def adder_maker():
    def inner_adder(a, b):
        global ADDER_CALLS_COUNTER
        ADDER_CALLS_COUNTER += 1
        return a + b
    return inner_adder


some_adder = adder_maker()
print(some_adder)  # тип - функция и локальной области видимости adder_maker
assert some_adder(1, 2) == 3
assert ADDER_CALLS_COUNTER == 2

"""
Hard
Перенесите глобальный счетчик на уровень объемлющей функции. Будет ли работать наш код?
Если да, то как поменялся смысл написанного кода? Если нет, то что надо изменить, чтобы всё заработало?
"""


def adder_maker():
    local_calls_counter = 0

    def inner_adder(a, b):
        nonlocal local_calls_counter  # если оставить global, будет неопределенная переменная в скоупе модуля
        local_calls_counter += 1
        print(local_calls_counter)
        return a + b
    return inner_adder


another_adder = adder_maker()
another_adder(1, 2)
another_adder(1, 2)
another_adder(1, 2)  # с каждым запуском выводится увеличивающеесяе значение local_calls_counter
