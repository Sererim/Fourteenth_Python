# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
from typing import List, Any, Tuple


def duplicate(lst: list[int], unique=1) -> list[Any] | tuple[Any, ...]:
    """
      Function that returns list of unique numbers in a list and duplicate numbers in a list.
      Function gets a list with numbers and a param unique.
      Unique equals to:
      - 1 returns list of unique numbers.
      - 2 returns list of duplicate numbers.
      - 3 returns a tuple with both lists in it.
      Everything else raises an Error.
      :return: tuple(unique_lst, duplicate_lst)
      """
    if lst is None or len(lst) == 0:
        raise ValueError("Error.\nList must have values.")
    elif len(lst) == 1:
        raise Exception("List must have at least two numbers in it.")

    d = {i: lst.count(i) for i in lst}
    duplicate_lst = [i for i in d.keys() if d.get(i) != 1]
    unique_lst = [i for i in d.keys() if d.get(i) == 1]

    match unique:
        case 1:
            return unique_lst
        case 2:
            return duplicate_lst
        case 3:
            temp = tuple(unique_lst) + tuple(duplicate_lst)
            return temp
        case _:
            raise AttributeError("Error!\n"
                                 "Unique param can be equal 1, 2 or 3.")
