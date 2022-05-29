"""
Easy.
1. Написать простую функцию, которая на вход принимает два числа и возвращает результат их сложения.
2. Записать эту функцию в произвольную переменную. Напечатать эту переменную на экран. Что вы видите?
3. Вызвать функцию суммирования через переменную, в которую вы только что её записали.
"""


def simple_sum(a, b):
    return a + b


summer = simple_sum

print(summer)  # видим ссылку на функцию simple_sum
sum_result = summer(-1, 1)  # которую тоже можем вызвать и получить a + b

"""
Medium.
1. Написать функцию, которая на вход будет принимать произвольное количество аргументов и возвращать их сумму.
2. В сигнатуре функции объявить 4 обязательных аргумента, но оставить возможность передавать в неё сколько угодно дополнительных аргументов.
Попробуйте вызвать функцию в следующих ситуациях и объясните результат:
    -прокинуть в функцию только 1 аргумент
    -прокинуть аргументы таким образом, чтобы обязательный аргумент был передан одновременно позиционно и по ключу
    -создать кортеж со значениями и распаковать его при вызове функции с помощью *
    -создать словарь со значениями и распаковать его при вызове функции с помощью * и **: что наблюдаете? Почему?
"""


def sum_of_many(first, second, third, fourth, *args):
    return sum([first, second, third, fourth, *args])


# sum_of_many(1)  # ожидается минимум 4 аргумента, а получен только first, TypeError

# sum_of_many(1, 2, 3, 4, first=1)  # даже если значение то же, и позиционно и по ключу нельзя передавать

arguments_tuple = 1, 2, 3, 4, 5, 6, 7
sum_of_many(*arguments_tuple)  # корректный результат

arguments_dict = {
    'first': 1,
    'second': 2,
    'third': 3,
    'fourth': 4,
}
# распакуются строковые ключи словаря, которые sum будет пытаться складывать с числовым аккумулятором, TypeError
# sum_of_many(*arguments_dict)
sum_of_many(**arguments_dict)  # с корректными аргументами корректный результат
arguments_dict['fifth'] = 5
# sum_of_many(**arguments_dict)  # а с некорректными неожиданный аргумент fifth, TypeError

"""
Hard.
Модифицировать функцию таким образом, чтобы для суммирования брались только обязательные аргументы,
первые 2 аргумента из дополнительных позиционных аргументов и любой аргумент из
дополнительных аргументов (если они есть), переданных по ключу (если они есть).
"""


from random import choice


def psycho_sum_of_many(first, second, third, fourth, *args, **kwargs):
    """Возвращает сумму обязательных аргументов, первых двух доп. позиционных и любого из кваргов, если возможно."""
    mandatory_sum = sum([first, second, third, fourth])

    additional_args_num = 2
    additional_sum = sum(args[:additional_args_num]) if len(args) >= additional_args_num else 0

    random_kwarg = choice(list(kwargs.values())) if kwargs else 0

    return mandatory_sum + additional_sum + random_kwarg


# psycho_sum_of_many(1)  # недостаточно обязятельных аргументов
print(psycho_sum_of_many(1, -1, 1, -1))  # ==0, складываем только переданные обязательные аргументв
print(psycho_sum_of_many(1, -1, 1, -1, 5))  # ==0, недостаточно дополнительных позиционных аргументов, надо минимум 2
print(psycho_sum_of_many(1, -1, 1, -1, 5, 2))  # == 7, достаточно доп. позиционных, их тоже складываем
print(psycho_sum_of_many(1, -1, 1, -1, 5, 2, 999, 1e100))  # == 7, складываем только первые два из доп. поцизионных
print(psycho_sum_of_many(1, -1, 1, -1, foo=5))  # == 5, всего один доп. кварг
print(psycho_sum_of_many(1, -1, 1, -1, foo=5, bar=2))  # == 5 или 2, выберем рандомный кварг
print(psycho_sum_of_many(1, -1, 1, -1, 5, 2, 999, 1e100, foo=3, bar=-7))  # == 10 или 0, все аргументы есть
