
"""
sequential_map - функция должна принимать в качестве аргументов любое количество функций
(позиционными аргументами, НЕ списком), а также контейнер с какими-то значениями.
Функция должна возвращать список результатов последовательного применения переданных функций
к значениям в контейнере. Например,
sequential_map(np.square, np.sqrt, lambda x: x**3, [1, 2, 3, 4, 5]) -> [1, 8, 27, 64, 125]
"""


def sequential_map(*args):
    *functions, values_ = args
    results = values_
    for func in functions:
        results = func(results)
    return results


""" 
consensus_filter - функция должна принимать в качестве аргументов любое количество функций 
(позиционными  аргументами, НЕ списком), возвращающих True или False, а также контейнер с какими-то значениями. 
Функция должна возвращать список значений, которые при передаче их во все функции дают True. 
Например: consensus_filter(lambda x: x > 0, lambda x: x > 5, lambda x: x < 10, [-2, 0, 4, 6, 11]) -> [6]
"""


def consensus_filter(*args):
    *functions, values_ = args
    for func in functions:
        if values_:
            passed = list(map(func, values_))
            values_ = [x for i, x in enumerate(values_) if passed[i]]
        else:
            break
    return values_


""" conditional_reduce - функция должна принимать 2 функции, а также контейнер со значениями. 
Первая функция должна принимать 1 аргумент и возвращать True или False, вторая также принимает 2 аргумента 
и возвращает значение (как в обычной функции reduce). conditional_reduce должна возвращать одно значение - 
результат reduce, пропуская значения с которыми первая функция выдала False. 
Например, conditional_reduce(lambda x: x < 5, lambda x, y: x + y, [1, 3, 5, 10]) -> 4
"""


def conditional_reduce(func_1, func_2, values):
    passed = list(map(func_1, values))
    values = [x for i, x in enumerate(values) if passed[i]]

    def reduce(values_to_reduce):
        if len(values_to_reduce) == 1:
            return values_to_reduce[0]
        else:
            x, y = values_to_reduce[:2]
            values_to_reduce = values_to_reduce[2:]
            values_to_reduce.insert(0, func_2(x, y))
        return reduce(values_to_reduce)

    if len(values) >= 2:
        return reduce(values)
    elif len(values) == 1:
        return values[0]


""" func_chain - функция должна принимать в качестве аргументов любое количество функций 
(позиционными  аргументами, НЕ списком). Функция должна возвращать функцию, объединяющую все 
переданные последовательным выполнением. Например, 
my_chain = func_chain(lambda x: x + 2, lambda x: (x/4, x//4)). my_chain(37) -> (9.75, 9). 
"""


def func_chain(*functions):

    def pipe(x, first_func, *remaining):
        pipeline = first_func(x)
        if remaining:
            for func in remaining:
                pipeline = func(pipeline)
        return pipeline

    return lambda x: pipe(x, *functions)


""" Реализовать функцию  multiple_partial - аналог функции partial, но которая принимает неограниченное 
число функций в качестве аргументов и возвращает список из такого же числа "частичных функций". 
Не используйте саму функцию partial. Например: 
ax1_mean, ax1_max, ax1_sum = multiple_partial(np.mean, np.max, np.sum, axis=1)
"""


def multiple_partial(*functions, **some_kwargs):
    return map(lambda x: lambda y: x(y, **some_kwargs), functions)

