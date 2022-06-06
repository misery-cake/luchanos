"""
Блок 3. Задача 1

1.1 Написать декоратор, который перед запуском произвольной функции с произвольным набором аргументов будет показывать
в консоли сообщение "Покупайте наших котиков!" и возвращать результат запущенной функции.
1.2 Параметризовать декоратор таким образом, чтобы сообщение, печатаемое перед выполнением функции можно было задавать
как параметр во время декорирования.
"""


def show_ad(func):
    def inner(*args, **kwargs):
        print('Покупайте наших котиков!')
        return func(*args, **kwargs)
    return inner


print_with_ad = show_ad(print)
print_with_ad('hello', 'world', end=' :-)\n')


def show_custom_ad(ad_text):

    def show_ad(func):

        def inner(*args, **kwargs):
            print(ad_text)
            return func(*args, **kwargs)

        return inner

    return show_ad


print_luchanos_ad = show_custom_ad('Смотрите youtube.com/luchanos')(print)
print_luchanos_ad('hello', 'world', end=' :-)\n')


@show_custom_ad('Подписывайтесь на телеграм чат')  # или с сахаром
def upper_case_print(text):
    print(text.upper())


upper_case_print('выведет капслоком и с надоедливой рекламой')
