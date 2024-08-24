import os
from typing import Any, Callable, Optional

from config import LOGS_PATH


def log(filename: Optional[str] = None) -> Callable:
    def my_decorator(func: Callable) -> Callable:
        def wrapper(*args: str) -> Any:
            try:
                func(*args)
                if filename:
                    with open(os.path.join(LOGS_PATH, filename), "w", encoding="UTF-8") as f:
                        f.write(f"{func.__name__} ок")
                        f.close()
                else:
                    print(f"{func.__name__} ок")
                return func
            except Exception as e:
                if filename:
                    with open(os.path.join(LOGS_PATH, filename), "w", encoding="UTF-8") as f:
                        f.write(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}")
                        f.close()
                else:
                    print(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}")

        return wrapper

    return my_decorator


@log()
def summ_my_int(a: int, b: int) -> int:
    return a + b


summ_my_int()
