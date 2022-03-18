list_one = []
list_two = ["dato uno", 2, True, "dato 4"]
print(list_two)
list_one.append("position 1")
# hacer un espacion he integrar un dato en la lista
list_two.insert(0, "pos 3")
print(list_two)

# extrae y elimina el ultimo valor de la lista
list_two.pop()
print(list_two)

# 'sort' ordena los valores de menor a mayor por defecto
list_numbers = [23, 23, 143, 1, 45, 6, 677, 43]
list_numbers.sort()
print(list_numbers)
# sort ordena al revers los numeros
list_numbers.sort(reverse = True)
print(list_numbers)

# unir listas
list_numer_one = [12, 43, 546, 2, 56, 76]
list_numer_one.sort()
list_numer_two = [32, 90]
list_numer_one.extend(list_numer_two)
print(list_numer_one)
list_numer_one.sort(reverse=True)
print(list_numer_one)