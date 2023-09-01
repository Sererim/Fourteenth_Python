# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


lst = [1, 1, 2, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 10]
d = {i: lst.count(i) for i in lst}
duplicate_lst = [i for i in d.keys() if d.get(i) != 1]
unique_lst = [i for i in d.keys() if d.get(i) == 1]

print(f"Original list:\n{lst}\n"
      f"List of duplicates:\n{duplicate_lst}\n"
      f"List of unique elements:\n{unique_lst}\n")
