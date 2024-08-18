from typing import Iterable, Union


def filter_by_state(my_list: Iterable[list], state: Union[str] = "EXECUTED") -> Iterable[list]:
    return [i for i in my_list if i["state"] == state]
