def val_checker(check):
    def wrapper(func):
        def val(res):
            if check(res):
                return func(res)
            else:
                raise ValueError(f'wrong val: {res}')
        return val
    return wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(-9)
print(a)
