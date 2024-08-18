from typing import Iterable, Union


def filter_by_state(my_list: Iterable[list], state: Union[str] = "EXECUTED") -> Iterable[list]:
    return [i for i in my_list if i["state"] == state]


def sort_by_date(my_list: Iterable[list], sort_descending: Union[bool] = 'True') -> Iterable[list]:
    return sorted(my_list, key=lambda x: x["date"], reverse=sort_descending)
