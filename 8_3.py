def type_logger(func):
    def first(**kwargs):
        result = [f'{func.__name__}({i}:{type(i)}),' for i in kwargs.values()]
        print(*result)

    return first


@type_logger
def calc_cub(x):
    return x ** 3


calc_cub(a=3, b=[], c='one', d=(1,))
