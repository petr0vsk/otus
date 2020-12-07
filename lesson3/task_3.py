######### библиотеки ######################################################################
from operator  import pow 
from itertools import repeat
from pprint import pprint
import time
from functools import wraps
########### функции #######################################################################
#--- декоратор измеряющий время выполнения функции ------
def timer(f):
    '''
    декоратор, возращает время выполнения функции в ms
    '''
    @wraps(f) # получите вашу wraps из functools
    def inner(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print( f"Время выполнения функции: { '{:.2f}ms'.format(1000*(time.time()-t))}" )
        return res
    return inner
# --- декоратор, подсчитвающий число вызовов (вхождений) функции --- 
def trace(str): # передаем в качестве аргумента строку для визуализации погружений/всплытий
    """
    Trace calls made to the decorated function.
    @trace("____")
    def fib(n):
        ....
    >>> fib(3)
     --> fib(3)
    ____ --> fib(2)
    ________ --> fib(1)
    ________ <-- fib(1) == 1
    ________ --> fib(0)
    ________ <-- fib(0) == 1
    ____ <-- fib(2) == 2
    ____ --> fib(1)
    ____ <-- fib(1) == 1
     <-- fib(3) == 3
    """
    def first_inner(f):
        count = 0 # инициализуруем счетчик
        @wraps(f)
        def second_inner(*args, **kwargs):
            nonlocal count
            print(f'{str*count} --> {f.__name__}({args[0]})') # всплываем...
            count += 1
            res = f(*args, **kwargs)
            count -= 1
            print(f'{str*count} <-- {f.__name__}({args[0]}) == {res}') # погружаемся... 
            return res
        return second_inner
    return first_inner    
# --- функция, которая принимает N целых чисел и возвращает список степеней этих чисел ---
def get_degree_of_numbers(*args, degree=2):
    """" 
    Функция принимает на вход произвольное количество целых чисел и возвращает (по умолчанию) 
    квадртную степень этих чисел. опциональный аргумент 'degree = ' позволяет 
    получить проивзольную степень числа.
    Ограничения: все аргументы целые (int) числа.
    """
    if isinstance(degree, int):  # степень целое число?
            if all(isinstance(x, int) for x in args): # все аргументы целые числа?
                return(list(map(pow, args, repeat(degree) ))) 
            else:
                print("=== Error: all argumrnts must be integer!!! ===") # если ошиблись с типом аргументов
                
    else:
        print("=== Error: degree must be integer!!! ===") # если ошиблись с типом аргументов
                       
# --- функция, которая на вход принимает список из целых чисел, и возвращает только чётные/нечётные/простые числа ---

DEF_RETURN_EVEN = 0  # константа по умолчанию для проверки типа фильтрации в UPPER_SNAKE_CASE
@timer
def get_even_odd_simple_num(*args, choise = DEF_RETURN_EVEN):
    """" 
    Функция принимает на вход список из целых чисел, 
    и возвращает только чётные/нечётные/простые числа 
    (выбор производится передачей дополнительного аргумента) choise = 0/1/2
    По умолчнию возвращает четные числа (см. константу DEF_RETURN_EVEN = 0 )
    Ограничения: все аргументы целые (int) числа.
    """
    #---- унутренняя функция для проверки является ли число простым ---   
    def is_num_simple(x):
        if x == 1:
            return False  # решением ООН еденица исключена из списка простых чисел
        if x % 2 == 0:
            return x == 2 # ура! простое число!
        d = 3
        while d * d <= x and x % d != 0:
            d += 2
        return d * d > x # а здесь возможны варинаты ...
    #----------------------------------------------------------------
    if all(isinstance(x, int) for x in args): # все аргументы целые числа?
        if choise == 0: # по умолчанию вернем четные числа из списка
            return list(filter(lambda x: x%2, args))     
        elif choise == 1: # вернем нечетные числа из списка
            return list(filter(lambda x: not x%2, args)) 
        elif choise == 2: # вернем простые числа из списка 
            return  list(filter(is_num_simple, args))    
        else:  
            print("=== Error: choise = 0/1/2 only!!! ===") # если ошиблись с богатством выбора
    else:
            print("=== Error: all argumrnts must be integer!!! ===")# если ошиблись с типом аргументов
    

# ---   ф. фибоначи рекурсивно --- 
@trace("____")
def fib(n):
    '''
    Вычисление n-го числа ряда Фибоначчи
    Соглашения: начинаем ряд с чиcла 1
    Ограничения: все аргументы целые (int) числа.
    '''
    if isinstance(n, int): 
        if n in (1, 2):
            return 1
        return fib(n - 1) + fib(n - 2) 
    else:
        print("=== Error: argument must be integer!!! ===")# если ошиблись с типом аргумента   

########################### демонстрируем работу всех функций #################################
def main():
    pprint('результат работы функции возведения в степень 3 списка чисел ')    
    pprint(list( get_degree_of_numbers(1,2,3,4,5, degree=3)  ))
    pprint('результат работы функции которая на вход принимает список из целых чисел, ')    
    pprint('и возвращает только чётные/нечётные/простые числа')
    pprint('+ работа декоратора, измеряющего время выполнения функции')
    pprint(list(get_even_odd_simple_num(1,2,3,4,5, choise = 0)))
    pprint(list(get_even_odd_simple_num(1,2,3,4,5, choise = 1)))
    pprint(list(get_even_odd_simple_num(1,2,3,4,5, choise = 2)))
    pprint(' работа обертки декоратора @wrap для ф. get_even_odd_simple_num()')
    pprint(get_even_odd_simple_num.__doc__)
    pprint('результат работы функции определения простого числа + декоратор @trace ')    
    pprint(fib(3))
    pprint(' работа обертки декоратора @wrap для ф. fib()')
    pprint(fib.__doc__)

if __name__ == '__main__':
    main()