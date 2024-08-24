import os
from config import LOGS_PATH


def log(filename = None):
    def my_decorator(func):
        def wrapper(*args):
            try:
                func(*args)
                if filename:
                    with open(os.path.join(LOGS_PATH, filename), 'w', encoding='UTF-8') as f:
                        f.write(f'{func.__name__} ок')
                        f.close()
                else:
                    print(f'{func.__name__} ок')
            except Exception as e:
                if filename:
                    with open(os.path.join(LOGS_PATH, filename), 'w', encoding='UTF-8') as f:
                        print(f)
                        f.write(f'{func.__name__} error: {type(e).__name__}. Inputs: {args}')
                        f.close()
                else:
                    print(f'{func.__name__} error: {type(e).__name__}. Inputs: {args}')
            return func
        return wrapper
    return my_decorator


@log('log.txt')
def summ_my_int(a, b):
    return a + b


summ_my_int('wq', 2)
